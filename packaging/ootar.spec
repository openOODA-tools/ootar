Name:           ootar
Version:        0.1.0
Release:        1%{?dist}
Summary:        Traversal-resistant archive manager with zero zip-slip vulnerability
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootar
Source0:        ootar-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootar is a sovereign, traversal-resistant archive manager (USTAR/tar) written
in pure openOODA, featuring zero-trust path sanitization against zip-slip exploits,
safe extraction gated by FsWriteCap, themed TOC listing, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootar
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootar-uninstall

%files
/usr/bin/ootar
/usr/bin/ootar-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign release: traversal resistance, safe extraction, and MCP stdio surface
