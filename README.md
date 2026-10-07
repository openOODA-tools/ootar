# ootar

> **Traversal-resistant archive manager with zero zip-slip vulnerability for the openOODA era.**  
> *A drop-in `tar` alternative written in pure openOODA, featuring zero-trust path sanitization against zip-slip directory traversal exploits, capability-gated safe extraction (`FsWriteCap`), themed archive listing, and a first-class Model Context Protocol (MCP) surface.*

Part of [openOODA-tools](https://github.com/openOODA-tools).

---

## 1. Installation

`ootar` has zero runtime dependencies. It compiles to a standalone native binary linked directly with libc.

### Universal Web Installer
Installs the standalone native binary to `/usr/local/bin` (or `~/.local/bin`):

```bash
curl -fsSL https://openooda-tools.github.io/ootar/install.sh | bash
```

### Debian / Ubuntu (APT)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/ootar/install.sh | bash -s -- --apt

# Or manual package install
sudo dpkg -i ootar_0.1.0-1_amd64.deb
```

### Fedora / RHEL / CentOS (DNF)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/ootar/install.sh | bash -s -- --dnf

# Or manual RPM install
sudo dnf install ./ootar-0.1.0-1.fc44.x86_64.rpm
```

### Arch Linux (PKGBUILD)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/ootar/install.sh | bash -s -- --arch

# Or manual build via packaging/PKGBUILD
cd packaging && makepkg -si
```

### Clean Uninstaller
To cleanly remove `ootar` and any installed package manager entries:

```bash
# Automated via standalone uninstaller
curl -fsSL https://openooda-tools.github.io/ootar/uninstall.sh | bash

# Or via installer flag
curl -fsSL https://openooda-tools.github.io/ootar/install.sh | bash -s -- --uninstall

# Or preview removal without making changes (dry-run)
curl -fsSL https://openooda-tools.github.io/ootar/uninstall.sh | bash -s -- --dry-run
```

---

## 2. Usage & Features

### Safe Archive Operations
Create, list, and safely extract standard USTAR archives:

```bash
# Create an archive from files
ootar -c -f backup.tar file1.txt file2.txt

# List table of contents with oote color styling
ootar -t -f backup.tar

# Safely extract files without risk of zip-slip attacks
ootar -x -f backup.tar -C /tmp/safe_dir
```

### Model Context Protocol (MCP) Server
`ootar` features a native Model Context Protocol (MCP) stdio server allowing AI pair programmers and LLM coding assistants to safely inspect tar archives:

```bash
ootar --mcp
```

#### Exposed MCP Tools:
- `inspect_archive`: Safely inspects archive table of contents and flags any unsafe entries.
- `safe_check`: Validates whether a file path violates directory traversal constraints (`../`, `/`).

---

## 3. License

Apache License 2.0. See [LICENSE](LICENSE) for details.