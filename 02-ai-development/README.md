# AI Development Learning Path

Build strong, practical Python skills by building a real tool: a **Tableau Workbook Review & Assistant app** — a Python application that reads `.twb`/`.twbx` files, understands their structure, flags issues, and uses an LLM to explain and improve calculated fields and workbook design.

This path trades the generic ML curriculum for applied Python + LLM-integration skills, since that's what the target project actually needs.

> **Real workbooks, kept local:** the whole point of this tool is reviewing workbooks you actually use, so practice against your own `.twb`/`.twbx` files. Drop them in [`workbooks/`](./workbooks/) — that folder is gitignored and its contents are never committed. Only sample/synthetic workbooks (if you make any) should ever go into git.

> **Vs. Path 4 (AI-Assisted Product Development):** this path teaches *calling* the Claude API from your own Python code (a technical skill). Path 4 teaches *using* AI as your development and planning collaborator while you build things — a different, meta-level skill. You'll use both together here.

## Learning Progression

### 📍 Level 1: Python Foundations for App Building (Week 1-2)
- Python fundamentals for tooling (not notebooks): modules, classes, dataclasses, type hints
- Working with files: `zipfile` (a `.twbx` is a zip bundle), `xml.etree.ElementTree` / `lxml`
- Parsing Tableau's XML structure: datasources, connections, calculated fields, worksheets, dashboards
- CLI basics with `argparse` or `typer`

### 📍 Level 2: Workbook Inspection & Linting (Week 3-4)
- Modeling a workbook as Python objects (`Workbook`, `Datasource`, `CalculatedField`, `Worksheet`)
- Building an inventory report: every data source, every calculated field and its formula, every worksheet/dashboard
- Rule-based "linting": unused fields, hardcoded constants in calculations, overly nested `IF`/`CASE` logic, blended data sources (a common performance smell), inconsistent field naming, missing field descriptions

### 📍 Level 3: LLM-Assisted Review (Week 5-6)
- Calling the Claude API from Python (`anthropic` SDK): auth, prompts, structured output
- Prompting for plain-English explanations of calculated field formulas
- Prompting for simplification/optimization suggestions on complex calcs
- Auto-generating field documentation/descriptions from formula + context
- Designing prompts that return structured (JSON) output you can act on programmatically

### 📍 Level 4: Packaging & Polish (Week 7-8)
- Turning the pieces into a single CLI tool: `tableau-review my_workbook.twbx`
- Output formats: terminal summary, Markdown/HTML report
- Config for which lint rules and LLM checks to run
- Testing with `pytest` (sample `.twbx` fixtures)
- Optional: expose it as a page in the Streamlit app from Path 3, so you can drag-and-drop a workbook and get a report in the browser

## 📚 Topics Covered

### Foundations
1. **Python for Tooling**
   - Classes and dataclasses to model structured data
   - Type hints for maintainability
   - Working with paths, zip archives, and XML
   - Error handling for malformed/unexpected files

2. **Understanding the Tableau File Format**
   - `.twb` (XML workbook) vs. `.twbx` (zipped package with extracts/resources)
   - Key XML elements: `<datasource>`, `<calculation>`, `<worksheet>`, `<dashboard>`, `<parameter>`
   - The [`tableaudocumentapi`](https://github.com/tableau/document-api-python) package as a higher-level alternative to raw XML parsing

3. **CLI Design**
   - Argument parsing, subcommands
   - User-friendly error messages and exit codes

### Inspection & Linting
4. **Structural Extraction**
   - Walking the XML tree to collect data sources, fields, and calculations
   - Mapping field dependencies (which calcs reference which fields)

5. **Lint Rules**
   - Unused field detection
   - Hardcoded value detection in formulas
   - Formula complexity heuristics
   - Naming convention checks
   - Data source blending / join risk flags

### LLM Integration
6. **Prompt Engineering for Code/Formula Review**
   - Giving the model formula + surrounding context (field name, data source, usage)
   - Asking for structured JSON responses (explanation, risk level, suggested rewrite)
   - Handling and validating LLM output before displaying/using it

7. **Documentation Generation**
   - Turning formulas + LLM explanations into a field data dictionary
   - Exporting as Markdown for sharing with the team

### Packaging
8. **Production Habits**
   - `pytest` test suite with sample workbooks
   - `requirements.txt` / dependency management
   - Config files (which rules to enable)
   - Logging instead of print statements

## 🎓 Projects

### Project 1: Tableau File Parser
**Level:** Beginner
**Skills:** File/zip/XML handling, data modeling
Parse a `.twb`/`.twbx` file and extract every data source and calculated field into Python objects; export the inventory to CSV.

### Project 2: Workbook Linter
**Level:** Intermediate
**Skills:** Rule-based analysis, dependency graphs
Implement the rule set above (unused fields, hardcoded values, naming, complexity, blending risk) and produce a workbook health-check report.

### Project 3: LLM-Powered Calculation Explainer & Optimizer
**Level:** Intermediate-Advanced
**Skills:** LLM API integration, prompt design, structured output
For each calculated field, get a plain-English explanation and an optional simplified/optimized rewrite from Claude. Auto-generate field documentation.

### Project 4: Tableau Workbook Assistant (full tool)
**Level:** Advanced
**Skills:** CLI packaging, testing, integration
Combine the parser, linter, and LLM reviewer into one CLI tool (and optionally a Streamlit front end) that takes a workbook and produces a full review report.

## 💻 Tech Stack

### Core Libraries
- **File parsing:** `zipfile`, `xml.etree.ElementTree` or `lxml`, `tableaudocumentapi`
- **LLM:** `anthropic` Python SDK (Claude)
- **CLI:** `argparse` or `typer`
- **Data/reporting:** `pandas` for tabular exports, `Jinja2` or Markdown for report generation
- **Testing:** `pytest`

### Tools
- VS Code
- Sample `.twbx` workbooks (your own, or Tableau's public sample workbooks) for test fixtures
- Tableau Desktop (to inspect ground truth while validating parsing logic)

## 💡 Learning Tips

1. **Start with one real workbook** - Pick a `.twbx` you actually use and get the parser working against it first
2. **Validate against Tableau itself** - Open the workbook in Tableau Desktop side-by-side to confirm your parser reads it correctly
3. **Design prompts iteratively** - Treat prompt-writing as its own coding task; test on varied formula complexity
4. **Keep LLM output structured** - Ask for JSON, validate it, don't trust free text for anything you'll act on programmatically
5. **Build the CLI early** - Even a rough CLI makes it much easier to test against multiple workbooks as you go

## 🤖 Working through this with AI

Default to tutor mode (see [`CLAUDE.md`](../CLAUDE.md)) — attempt the parsing/lint logic yourself first. Example prompts:
- "Explain how `.twbx` zip structure relates to `.twb` XML, then let me try writing the extraction function before you show me one."
- "Here's my first pass at the unused-field lint rule [paste]. Don't rewrite it — tell me what edge case it misses and ask me a question that gets me there."
- "Quiz me on when to use `ElementTree` vs. `tableaudocumentapi` before I pick one for the parser."

## 📖 Resources

### Tableau File Format
- [Tableau Document API (Python)](https://github.com/tableau/document-api-python)
- [Tableau's `.twb` XML reference (community documentation)](https://www.tableau.com/support)

### LLM/Anthropic
- [Anthropic API Documentation](https://docs.claude.com/)
- [Claude Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Prompt Engineering Guide](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

### Python
- [Real Python: Working with XML](https://realpython.com/python-xml-parser/)
- [Python `zipfile` docs](https://docs.python.org/3/library/zipfile.html)
- [`typer` documentation](https://typer.tiangolo.com/)

## 🚀 Next Steps

If you haven't already, build the [Work Tracker MVP](../03-streamlit-development/README.md) first and use it to track this project's tasks. From here:
1. Apply **Advanced SQL** skills if the assistant ever needs to log review history or metrics in a database
2. Build a **Streamlit** front end for the assistant, or fold it into the work tracker app
3. Use **AI-Assisted Product Development** to practice the draft-then-review workflow on the linter/LLM-review code

---

**Ready to start?** Grab a real `.twbx` file and start Project 1 — get the calculated fields printed to the console.
