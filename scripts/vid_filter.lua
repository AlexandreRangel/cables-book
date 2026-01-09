-- Pandoc Lua filter: render ```vid fenced code blocks as a "video card" in LaTeX.
--
-- Requirements implemented:
-- 1) Thumbnail image (33% of column width, controlled by \YouTubeThumbnailWidthFraction)
-- 2) URL
-- 3) Title
-- 4) Author
-- And keep the whole block together (no split across columns/pages).

local function trim(s)
  return (s:gsub("^%s+", ""):gsub("%s+$", ""))
end

local function latex_escape(s)
  -- Minimal LaTeX escaping for text fields (not URLs).
  local rep = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{",
    ["}"] = "\\}",
    ["$"] = "\\$",
    ["&"] = "\\&",
    ["#"] = "\\#",
    ["_"] = "\\_",
    ["%"] = "\\%",
    ["~"] = "\\textasciitilde{}",
    ["^"] = "\\textasciicircum{}",
  }
  return (s:gsub("[\\{}%$&#_~%^]", rep))
end

local function youtube_id_from_url(url)
  if not url then return nil end
  url = trim(url)
  local id =
    url:match("youtu%.be/([%w_%-%+]+)") or
    url:match("youtube%.com/watch%?v=([%w_%-%+]+)") or
    url:match("youtube%.com/shorts/([%w_%-%+]+)") or
    url:match("youtube%.com/embed/([%w_%-%+]+)")
  if not id then return nil end
  id = id:gsub("[?&].*$", "")
  return id
end

local function parse_vid_block(text)
  local url, title, author
  for line in text:gmatch("[^\r\n]+") do
    line = trim(line)
    if line ~= "" then
      if not url then
        url = line
      else
        local t = line:match("^Title:%s*(.*)$")
        local a = line:match("^Author:%s*(.*)$")
        if t then title = trim(t) end
        if a then author = trim(a) end
      end
    end
  end
  return url, title, author
end

local function path_join(a, b)
  if not a or a == "" then return b end
  if not b or b == "" then return a end
  local sep = "/"
  a = a:gsub("\\", "/")
  b = b:gsub("\\", "/")
  if a:sub(-1) == "/" then
    return a .. b
  end
  return a .. sep .. b
end

local function render_vid_card(url, title, author)
  local vid = youtube_id_from_url(url)
  local thumb_path = nil
  if vid then
    local cwd = "."
    if pandoc.system and pandoc.system.get_working_directory then
      cwd = pandoc.system.get_working_directory()
    end
    thumb_path = path_join(cwd, "chapters/images/youtube_thumbs/" .. vid .. ".jpg")
  end

  local lines = {}
  table.insert(lines, "\\needspace{9\\baselineskip}")
  -- Override mdframed spacing so we can control "between cards" spacing precisely.
  table.insert(lines, "\\begin{mdframed}[style=videocardstyle,skipabove=0pt,skipbelow=0pt]")
  table.insert(lines, "\\begingroup")
  table.insert(lines, "\\fontsize{\\VideoCardFontSizePt pt}{\\VideoCardLeadingPt pt}\\selectfont")
  table.insert(lines, "\\noindent\\begin{minipage}{\\linewidth}")

  if thumb_path then
    table.insert(
      lines,
      string.format(
        "\\noindent\\href{%s}{\\tikz[baseline]{\\node[inner sep=0pt,rounded corners=\\YouTubeThumbCornerRadius,clip]{\\includegraphics[width=\\YouTubeThumbnailWidthFraction\\linewidth,keepaspectratio]{\\detokenize{%s}}};}}\\par\\vspace{0.35\\baselineskip}",
        url,
        thumb_path
      )
    )
  end

  table.insert(lines, string.format("\\noindent\\small\\url{%s}\\par", url))

  if title and title ~= "" then
    table.insert(lines, string.format("\\noindent\\fontsize{\\VideoCardTitleFontSizePt pt}{\\VideoCardTitleLeadingPt pt}\\fontseries{sb}\\selectfont %s\\par", latex_escape(title)))
  end
  if author and author ~= "" then
    table.insert(lines, string.format("\\noindent\\small\\mdseries by %s\\par", latex_escape(author)))
  end

  table.insert(lines, "\\end{minipage}")
  table.insert(lines, "\\endgroup")
  table.insert(lines, "\\end{mdframed}")

  return pandoc.RawBlock("latex", table.concat(lines, "\n"))
end

function Pandoc(doc)
  -- Only rewrite for LaTeX/PDF builds; keep original for other formats.
  if FORMAT ~= "latex" then
    return doc
  end

  local out = pandoc.List()
  local prev_was_vid = false

  for _, blk in ipairs(doc.blocks) do
    if blk.t == "CodeBlock" and blk.classes and blk.classes:includes("vid") then
      local url, title, author = parse_vid_block(blk.text)
      if url then
        if prev_was_vid then
          out:insert(pandoc.RawBlock("latex", "\\par\\vspace{\\VideoCardSpacingBetweenCards}"))
        else
          out:insert(pandoc.RawBlock("latex", "\\par\\vspace{\\VideoCardSpacingBefore}"))
        end
        out:insert(render_vid_card(url, title, author))
        prev_was_vid = true
      else
        out:insert(blk)
        prev_was_vid = false
      end
    else
      out:insert(blk)
      prev_was_vid = false
    end
  end

  doc.blocks = out
  return doc
end


