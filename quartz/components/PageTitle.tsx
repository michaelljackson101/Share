import { pathToRoot } from "../util/path"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

function PageTitle({ fileData, cfg }: QuartzComponentProps) {
  const title = cfg?.pageTitle ?? "Untitled Quartz"
  const baseDir = pathToRoot(fileData.slug!)

  return (
    <div class="page-title">
      <a class="brand" href={baseDir} aria-label={title}>
        <img class="logo" src={`${baseDir}/static/IF-AI-blue.png`} alt="" />
        <span class="brand-text">{title}</span>
      </a>
    </div>
  )
}

PageTitle.css = `
.page-title { margin: 0; }
.brand { display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none; }
.logo { height: 96px; width: auto; }
.brand-text { font-weight: 700; }
`

export default (() => PageTitle) satisfies QuartzComponentConstructor
