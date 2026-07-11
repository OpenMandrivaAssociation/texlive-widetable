%global tl_name widetable
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	An environment for typesetting tables of specified width
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/widetable
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a new environment that, unlike tabularX, typesets a
table of specified width by working on the inter-column glue; the
tabular cells will all be stretched (or shrunk) according to need. The
package will use the e-TeX arithmetic extensions if they are available
(they are, in most modern distributions).

