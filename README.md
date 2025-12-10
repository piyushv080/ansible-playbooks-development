# Ansible Playbooks Development

This is a personal learning repository where I (piyushv080) experiment, learn, and build Ansible playbooks by doing. The goal is to gather practical examples, notes, and small projects that helped me understand Ansible concepts and real-world automation tasks.

Languages used in this repository: Powershell, Python, Shell (examples, helper scripts, and static docs).

## Table of Contents

- [About](#about)
- [What you'll find here](#what-youll-find-here)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Examples & common commands](#examples--common-commands)
- [Repository layout](#repository-layout)
- [How I learned / Notes](#how-i-learned--notes)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

This repository documents my journey learning Ansible through practical playbooks and small projects. Each directory typically contains a self-contained example (inventory, playbook, roles, and README) that demonstrates a concept or task such as provisioning, configuration, templating, or orchestration.

## What you'll find here

- Reusable Ansible playbooks and role examples.
- Inventories and environment-specific sample files.
- Helper scripts (Python/Shell) used to generate inputs or post-process results.
- HTML notes and mini-docs summarizing lessons learned and references.

## Requirements

- Ansible (>= 2.9 recommended, but many examples work with newer versions)
- Python 3 (for some helper scripts)
- ssh access to hosts (for remote playbooks)
- Optional: Docker or local Vagrant for local testing

Install Ansible (example):
```bash
pip install --user ansible
# or
sudo apt update && sudo apt install -y ansible
```

## Quick start

1. Clone the repository:
```bash
git clone https://github.com/piyushv080/ansible-playbooks-development.git
cd ansible-playbooks-development
```

2. Inspect an example directory (each example has its own README):
```bash
ls -la
cat examples/some-playbook/README.md
```

3. Run a playbook against an inventory:
```bash
ansible-playbook -i inventories/dev_inventory playbooks/site.yml
# or a simple playbook:
ansible-playbook -i inventory.ini playbook.yml --check
```

Use --check to perform a dry run. Use --diff to show changes to files/templates.

## Examples & common commands

- Run a single role/play:
```bash
ansible-playbook playbooks/<playbook-name>.yml -i inventories/<inventory>
```

- Run ad-hoc command:
```bash
ansible all -i inventories/dev -m shell -a "uptime"
```

- Vault usage (encrypt a file):
```bash
ansible-vault encrypt group_vars/all/vault.yml
ansible-playbook playbooks/site.yml --ask-vault-pass
```

## Repository layout

A typical structure used here:
```
.
├── playbooks/               # top-level playbooks that call roles
├── roles/                   # reusable roles (tasks, handlers, defaults, templates)
├── inventories/             # sample inventories (dev, staging, prod)
├── examples/                # small self-contained examples with README
├── scripts/                 # helper Python/Shell scripts
├── docs/                    # HTML notes and learning material
└── README.md
```

Look inside each example for its own README explaining goals and how to run it.

## How I learned / Notes

- I focused on small, repeatable examples: one concept per playbook or role.
- I used local VMs or containers for testing before applying to remote hosts.
- I tried to keep playbooks idempotent and documented the expected state in each example's README.
- Common topics covered: inventory management, templating with Jinja2, roles and includes, handlers, Ansible Vault, and minimal testing with --check.

## Contributing

This is a personal learning repo — contributions are welcome but optional. If you want to suggest improvements or send a PR:

- Open an issue describing the change.
- Keep changes small and focused.
- Add or update the example README explaining the concept and how to test it.

## License

MIT License — see LICENSE file for details (or add one if you want).

## Contact

GitHub: https://github.com/piyushv080

Thanks for checking out my Ansible playground. If you'd like, I can:
- push this README into the repository,
- help add a CONTRIBUTING.md or LICENSE,
- or create a small example playbook to demonstrate a particular topic (inventory, roles, or Vault).
