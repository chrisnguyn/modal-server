# modal-server
Flask web server hosted on Modal infra

## Setup
`python3 -m venv venv`

`.zshrc`
- `eval "$(direnv hook zsh)"`
- `export DIRENV_LOG_FORMAT=""`

`echo "source venv/bin/activate" > .envrc`

`direnv allow`


## Deployment
`modal deploy src.main`
