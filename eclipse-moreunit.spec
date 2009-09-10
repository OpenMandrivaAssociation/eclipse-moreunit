%define src_repo_tag   V_1_2_0
%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_datadir}/eclipse/dropins/moreunit

Name:           eclipse-moreunit
Version:        1.2.0
Release:        %mkrel 2
Summary:        An Eclipse plugin that assists with writing more unit tests

Group:          Development/Other
License:        EPL
URL:            http://moreunit.sourceforge.net
## sh %{name}-fetch-src.sh V_1_2_0
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.4.0
Requires: eclipse-platform >= 3.4.0
Requires: eclipse-jdt

%description
MoreUnit is an Eclipse plugin that should assist with writing more unit tests.
It can decorate classes which have testcase(s) and mark methods in the editor
which are under test.  Renaming/moving classes/methods will cause moreUnit to
rename/move the corresponding test code.  Generation of test method stubs is
also possible.

%prep
%setup -q -c

%build
%{eclipse_base}/buildscripts/pdebuild -f moreUnit

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/moreUnit.zip

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc eclipse-moreunit-fetched-src-V_1_2_0/org.moreunit.plugin/help/documentation.html
