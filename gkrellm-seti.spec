Summary:	SETI@Home monitor plugin for gkrellm
Summary(pl):	Plugin gkrellm z monitorem SETI@Home
Name:		gkrellm-seti
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://xavier.serpaggi.free.fr/seti/seti-%{version}.tar.bz2
Patch0:		%{name}-makefile.patch
URL:		http://xavier.serpaggi.free.fr/seti/
BuildRequires:	gkrellm-devel >= 1.2.2
Requires:	gkrellm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A GKrellM plugin which lets you monitor your SETI@Home progress.

%description -l pl
Plugin GKrellM pozwalaj±cy monitorowaæ twoje postêpy w SETI@Home.

%prep
%setup -q -n seti-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog TODO

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm/seti.so
