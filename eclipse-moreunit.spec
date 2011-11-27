%global src_repo_tag   V_2_4_1
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/moreunit

Name:           eclipse-moreunit
Version:        2.4.1
Release:        3
Summary:        An Eclipse plugin that assists with writing more unit tests

Group:          Development/Java
License:        EPL
URL:            http://moreunit.sourceforge.net
## sh %{name}-fetch-src.sh V_2_4_1 2.4.1
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-fetch-src.sh

BuildArch: noarch

BuildRequires: eclipse-pde >= 0:3.6.0
Requires: eclipse-jdt >= 3.6.0

%description
MoreUnit is an Eclipse plugin that should assist with writing more unit tests.
It can decorate classes which have testcase(s) and mark methods in the editor
which are under test.  Renaming/moving classes/methods will cause moreUnit to
rename/move the corresponding test code.  Generation of test method stubs is
also possible.

%prep
%setup -q 

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
%{eclipse_base}/buildscripts/pdebuild -f org.moreunit

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.moreunit.zip 

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.moreunit.plugin/help/documentation.html

