%include /usr/lib/rpm/macros.perl
Summary:	GLgraph visualize mathematical functions
Summary(pl):	Narzêdzie do wizualizacji funkcji matematycznych
Name:		glgraph
Version:	0.2.6
Release:	0.1
License:	GPL v2
Group:		Applications/Math
Source0:	http://glgraph.kaosu.ch/downl/%{name}_%{version}.tar.bz2
# Source0-md5:	6fb17521170701f83d035b48df9db02b
URL:		http://glgraph.kaosu.ch/
BuildRequires:	rpm-perlprov
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLgraph is an interactive OpenGL based function grapher for Linux
written in Perl. It visualizes any mathematical function in 1, 2 or 3
unkowns (x,z,t) in a 2D, 3D or 4D wireframe or solid surface,
optionally with axis. It creates an animation after one time periode.
GLgraph has an command line interface to input a function, to specify
the minimum and maximum plotting bound and more. It can be
interactively controlled with the keyboard.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_bindir}/%{name}
