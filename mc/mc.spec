Summary:   User-friendly text console file manager and visual shell
Name:      mc
Version:   4.8.8
Release:   1%{?dist}
Epoch:     2
License:   GPLv2
Group:     System Environment/Shells

Source:    http://ftp.midnight-commander.org/mc-%{version}.tar.bz2
URL:       http://www.midnight-commander.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel
BuildRequires: e2fsprogs-devel
BuildRequires: slang-devel
BuildRequires: pcre-devel
BuildRequires: gpm-devel

%description
GNU Midnight Commander is a visual file manager.  It's a feature rich
full-screen text mode application that allows you to copy, move and
delete files and whole directory trees, search for files and run
commands in the subshell.  Internal viewer and editor are included.
Mouse is supported under X Window System and on Linux console.  VFS
(Virtual Filesystem) allows you to view archives and files on remote
servers (via SAMBA, FTP or SSH).

%prep
%setup

%build
%configure \
	--with-screen=slang \
	--enable-charset \
	--enable-vfs-smb \
	--with-samba \
	--with-x \
	--with-gpm-mouse
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot}

%{__install} -d -m 755 %{buildroot}/%{_sysconfdir}/profile.d
%{__install} contrib/{mc.sh,mc.csh} %{buildroot}/%{_sysconfdir}/profile.d

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)

%doc doc/FAQ COPYING doc/NEWS doc/README
%{_bindir}/mc
%{_bindir}/mcedit
%{_bindir}/mcview
%{_bindir}/mcdiff
%attr(4755, vcsa, tty) %{_libexecdir}/mc/cons.saver
%{_libexecdir}/mc/mc*sh
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/mc.1*
%lang(hu) %{_mandir}/hu/man1/mc.1*
%lang(it) %{_mandir}/it/man1/mc.1*
%lang(pl) %{_mandir}/pl/man1/mc.1*
%lang(ru) %{_mandir}/ru/man1/mc.1*
%lang(sr) %{_mandir}/sr/man1/mc.1*

%{_sysconfdir}/profile.d/*

%config %{_sysconfdir}/mc/sfs.ini

%config(noreplace) %{_sysconfdir}/mc/*edit*
%config(noreplace) %{_sysconfdir}/mc/mc.ext
%config(noreplace) %{_sysconfdir}/mc/mc.menu
%config(noreplace) %{_sysconfdir}/mc/filehighlight.ini
%config(noreplace) %{_sysconfdir}/mc/mc.keymap
%config(noreplace) %{_sysconfdir}/mc/mc.default.keymap
%config(noreplace) %{_sysconfdir}/mc/mc.emacs.keymap
%config(noreplace) %{_sysconfdir}/mc/mc.menu.sr
%dir %{_datadir}/mc
%{_datadir}/mc/*

%dir %{_libexecdir}/mc
%{_libexecdir}/mc/ext.d/*
%{_libexecdir}/mc/extfs.d/*
%{_libexecdir}/mc/fish/*

%changelog
* Sun Jun 16 2013 Denis Fateyev <denis@fateyev.com> - 4.8.8-1
- rebuild for Repoforge
