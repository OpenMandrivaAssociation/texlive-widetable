Name:		texlive-widetable
Version:	1.5
Release:	1
Summary:	An environment for typesetting tables of specified width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/widetable
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a new environment that, unlike tabularX,
typesets a table of specified width by working on the inter-
column glue; the tabular cells will all be stretched (or
shrunk) according to need. The package will use the e-TeX
arithmetic extensions if they are available (they are, in most
modern distributions).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/widetable
%doc %{_texmfdistdir}/doc/latex/widetable
#- source
%doc %{_texmfdistdir}/source/latex/widetable

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
