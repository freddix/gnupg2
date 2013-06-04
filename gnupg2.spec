Summary:	GNU Privacy Guard - secure communication and data storage
Name:		gnupg2
Version:	2.0.20
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/GnuPG/gnupg/gnupg-%{version}.tar.bz2
# Source0-md5:	9d18ee71bb0b10d40d1c8a393bdd7a89
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libassuan-devel
BuildRequires:	libcap-devel
BuildRequires:	libksba-devel
BuildRequires:	libusb-compat-devel
BuildRequires:	openldap-devel
BuildRequires:	pth-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
Requires:	pinentry
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnupg

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%package plugin-keys-curl
Summary:	GnuPG plugin for allow talk to a HTTP/FTP keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-curl
GnuPG plugin for allow talk to a HTTP(S)/FTP(S) keyserver.

%package plugin-keys-finger
Summary:	GnuPG plugin for allow talk to a FINGER keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-finger
GnuPG plugin for allow talk to a FINGER keyserver.

%package plugin-keys-hkp
Summary:	GnuPG plugin for allow talk to a HKP keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-hkp
GnuPG plugin for allow talk to a HKP keyserver.

%package plugin-keys-ldap
Summary:	GnuPG plugin for allow talk to a LDAP keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-ldap
GnuPG plugin for allow talk to a LDAP keyserver.

%prep
%setup -qn gnupg-%{version}

%build
cp -f /usr/share/automake/config.sub scripts
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/gpg-connect-agent
%attr(755,root,root) %{_bindir}/gpg2
%attr(755,root,root) %{_bindir}/gpgconf
%attr(755,root,root) %{_bindir}/gpgkey2ssh
%attr(755,root,root) %{_bindir}/gpgparsemail
%attr(755,root,root) %{_bindir}/gpgsm
%attr(755,root,root) %{_bindir}/gpgsm-gencert.sh
%attr(755,root,root) %{_bindir}/gpgv2
%attr(755,root,root) %{_bindir}/kbxutil
%attr(755,root,root) %{_bindir}/watchgnupg
%attr(755,root,root) %{_sbindir}/addgnupghome
%attr(755,root,root) %{_sbindir}/applygnupgdefaults

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnupg-pcsc-wrapper
%attr(755,root,root) %{_libexecdir}/gpg-check-pattern
%attr(755,root,root) %{_libexecdir}/gpg-preset-passphrase
%attr(755,root,root) %{_libexecdir}/gpg-protect-tool
%attr(755,root,root) %{_libexecdir}/scdaemon

%dir %{_datadir}/gnupg
%{_datadir}/gnupg/com-certs.pem
%{_datadir}/gnupg/gpg-conf.skel
%{_datadir}/gnupg/qualified.txt

# TODO: remaining intl files
%{_datadir}/gnupg/help.txt
%lang(de) %{_datadir}/gnupg/help.de.txt
%lang(pl) %{_datadir}/gnupg/help.pl.txt

%{_infodir}/gnupg.info*
%{_mandir}/man1/gpg-agent.1*
%{_mandir}/man1/gpg-connect-agent.1*
%{_mandir}/man1/gpg-preset-passphrase.1*
%{_mandir}/man1/gpg2.1*
%{_mandir}/man1/gpgconf.1*
%{_mandir}/man1/gpgparsemail.1*
%{_mandir}/man1/gpgsm-gencert.sh.1*
%{_mandir}/man1/gpgsm.1*
%{_mandir}/man1/gpgv2.1*
%{_mandir}/man1/scdaemon.1*
%{_mandir}/man1/symcryptrun.1*
%{_mandir}/man1/watchgnupg.1*
%{_mandir}/man8/addgnupghome.8*
%{_mandir}/man8/applygnupgdefaults.8*

%files plugin-keys-finger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_finger

%files plugin-keys-hkp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_hkp

%files plugin-keys-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_curl

%files plugin-keys-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_ldap

