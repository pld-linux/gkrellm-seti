Summary:	SETI@Home monitor plugin for gkrellm
Summary(pl):	Plugin gkrellm z monitorem SETI@Home
Name:		gkrellm-seti
Version:	0.7.0b
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://xavier.serpaggi.free.fr/seti/seti-%{version}.tar.bz2
# Source0-md5:	bea7ca090a486560207544c1f665a2c1
Patch0:		http://xavier.serpaggi.free.fr/seti/seti-0.7.0b-gkrellm2.diff
URL:		http://xavier.serpaggi.free.fr/seti/
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GKrellM plugin which lets you monitor your SETI@Home progress.

%description -l pl
Plugin GKrellM pozwalaj±cy monitorowaæ swoje postêpy w SETI@Home.

%prep
%setup -q -n seti-%{version}
%patch0 -p1

%build
# typo - two different variables for optflags
%{__make} \
	CC="%{__cc}" \
	DBGFLAGS="%{rpmcflags}" \
	DGBFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D seti.so $RPM_BUILD_ROOT%{_libdir}/gkrellm/seti.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_libdir}/gkrellm/seti.so
