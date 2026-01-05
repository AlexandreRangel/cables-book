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

function CodeBlock(el)
  if not el.classes:includes("vid") then
    return nil
  end

  -- Only rewrite for LaTeX/PDF builds; keep original for other formats.
  if FORMAT ~= "latex" then
    return nil
  end

  local url, title, author = parse_vid_block(el.text)
  if not url then
    return nil
  end

  local vid = youtube_id_from_url(url)
  local thumb_path = nil
  if vid then
    -- Pandoc runs XeLaTeX in a temp media directory; relative paths in raw LaTeX
    -- won't work (and Pandoc won't copy media referenced only in raw LaTeX).
    -- Use an absolute path so XeLaTeX can always find the cached thumbnail.
    local cwd = "."
    if pandoc.system and pandoc.system.get_working_directory then
      cwd = pandoc.system.get_working_directory()
    end
    thumb_path = path_join(cwd, "chapters/images/youtube_thumbs/" .. vid .. ".jpg")
  end

  local lines = {}
  table.insert(lines, "\\needspace{8\\baselineskip}")
  table.insert(lines, "\\noindent\\begin{minipage}{\\linewidth}")

  if thumb_path then
    table.insert(
      lines,
      string.format(
        "\\noindent\\includegraphics[width=\\YouTubeThumbnailWidthFraction\\linewidth,keepaspectratio]{\\detokenize{%s}}\\par\\vspace{0.35\\baselineskip}",
        thumb_path
      )
    )
  end

  table.insert(lines, string.format("\\noindent\\small\\url{%s}\\par", url))

  if title and title ~= "" then
    table.insert(lines, string.format("\\noindent\\small\\textbf{Title:} %s\\par", latex_escape(title)))
  end
  if author and author ~= "" then
    table.insert(lines, string.format("\\noindent\\small\\textbf{Author:} %s\\par", latex_escape(author)))
  end

  table.insert(lines, "\\end{minipage}\\par\\vspace{0.75\\baselineskip}")

  return pandoc.RawBlock("latex", table.concat(lines, "\n"))
end


