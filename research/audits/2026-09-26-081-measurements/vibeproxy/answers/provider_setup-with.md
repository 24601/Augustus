I haven't installed anything yet because the working directory (`/private/tmp/e-4cgHkA/home/cwd`) looks empty:

- **No project files.** There's no `package.json`, `pyproject.toml`, `go.mod`, or source code, so I can't tell which language's SDK to install or which package manager to use.
- **No `.env` file.** There's no API key in this directory for me to wire up.
- **Nothing mentions "TypeSafe"** anywhere under your home directory, so I have no install instructions or package name to go on.

To go ahead, I need:

1. **The right directory.** Is the project somewhere else, or should I start a new one here? If it's new, which language and package manager (for example Node with npm or pnpm, or Python with uv or pip)?
2. **The SDK's package name or docs link.** For example, the npm or PyPI name. I don't want to guess a name and install a lookalike package.
3. **Where your `.env` file is,** and the variable name the SDK expects (for example `TYPESAFE_API_KEY`). Please don't paste the key itself here. I'll read it from `.env` and make sure `.env` is in `.gitignore`.
