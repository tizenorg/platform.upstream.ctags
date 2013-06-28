Name:           ctags
Version:        5.8
Release:        0
License:        GPL-2.0+
Summary:        Tool for generating indexes of source code definitions
Url:            http://ctags.sourceforge.net/
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Source1001: 	ctags.manifest

%description
Exuberant Ctags is a multilanguage reimplementation of the much-underused
ctags(1) program and is intended to be the mother of all ctags programs. It
generates indexes of source code definitions which are used by a number of
editors and tools. The motivation which drove the development of Exuberant
Ctags was the need for a ctags program which supported generation of tags
for all possible C language constructs (which no other ctags offers), and
because most were easily fooled by a number of preprocessor contructs.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/ctags
