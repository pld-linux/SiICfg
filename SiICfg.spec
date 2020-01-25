Summary:	SiImage SATARAID Management Utility for Linux
Summary(pl.UTF-8):	Narzędzie do zarządzania SATARAID-em SiImage dla Linuksa
Name:		SiICfg
Version:	1.21
Release:	0.3
License:	?
Group:		Development/Languages/Java
Source0:	http://www.siliconimage.com/docs/RAID_GUI_v%{version}.tar.gz
# NoSource0-md5:	49e8716dba710a975fb1e7a28376c2be
NoSource:	0
URL:		http://www.siliconimage.com/support/supportsearchresults.aspx?pid=29&cid=11&ctid=2&osid=2
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
Requires:	jre > 1.4
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
SiImage SATARAID Management Utility for Linux supports RAID 0, 1, and
10.

Use this tool with the latest SATARAID drivers and BIOS:
- Latest SiI3x12 driver: 1.0.0.51
- Latest SiI3114 driver: 1.0.0.8
- Latest SiI3x12 BIOS: 4.2.50
- Latest SiI3114 BIOS: 5.0.52

%description -l pl.UTF-8
SATARAID Management Utility to narzędzie do zarządzania SATARAID-em
SiImage dla Linuksa. Obsługuje RAID 0, 1 i 10.

Narzędzie powinno być używane z najnowszymi sterownikami i BIOS-em
SATARAID:
- sterownik SiI3x12: 1.0.0.51
- sterownik SiI3114: 1.0.0.8
- BIOS SiI3x12: 4.2.50
- BIOS SiI3114: 5.0.52

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -n RAID_GUI
cd %{name}
%{__sed} -i -e 's,\r$,,' *.properties
cat > %{name}.sh <<'EOF'
#!/bin/sh
cd %{_appdir}
%if "%{_lib}" != "lib"
export LD_LIBRARY_PATH=%{_libdir}
%endif
exec java -cp %{_appdir}/classes:%{_appdir}/classes/jh.jar:%{_appdir}/classes/mail.jar siicfg.SiICfgMain
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_libdir},%{_bindir}}
cd %{name}
cp -a classes image $RPM_BUILD_ROOT%{_appdir}
cp -a *.library *.properties vssver.scc $RPM_BUILD_ROOT%{_appdir}
%ifarch %{ix86}
install libSiCommand_i386.so $RPM_BUILD_ROOT%{_libdir}/libSiCommand.so
%endif
%ifarch %{x8664}
install libSiCommand_x86_64.so $RPM_BUILD_ROOT%{_libdir}/libSiCommand.so
%endif
install %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libSiCommand.so
%{_appdir}

%files doc
%defattr(644,root,root,755)
%doc SiI_GUI.doc "SATARaid\ Manual.doc"
%doc SiICfg/doc/*
