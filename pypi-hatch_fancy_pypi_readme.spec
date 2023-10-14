#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-hatch_fancy_pypi_readme
Version  : 23.1.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/85/a6/58d585eba4321bf2e7a4d1ed2af141c99d88c1afa4b751926be160f09325/hatch_fancy_pypi_readme-23.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/a6/58d585eba4321bf2e7a4d1ed2af141c99d88c1afa4b751926be160f09325/hatch_fancy_pypi_readme-23.1.0.tar.gz
Summary  : Fancy PyPI READMEs with Hatch
Group    : Development/Tools
License  : MIT
Requires: pypi-hatch_fancy_pypi_readme-bin = %{version}-%{release}
Requires: pypi-hatch_fancy_pypi_readme-license = %{version}-%{release}
Requires: pypi-hatch_fancy_pypi_readme-python = %{version}-%{release}
Requires: pypi-hatch_fancy_pypi_readme-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Your ✨Fancy✨ Project Deserves a ✨Fancy✨ PyPI Readme!
[![PyPI - Version](https://img.shields.io/pypi/v/hatch-fancy-pypi-readme.svg)](https://pypi.org/project/hatch-fancy-pypi-readme)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-fancy-pypi-readme.svg)](https://pypi.org/project/hatch-fancy-pypi-readme)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![License: MIT](https://img.shields.io/badge/license-MIT-C06524)](https://github.com/hynek/hatch-fancy-pypi-readme/blob/main/LICENSE.txt)

%package bin
Summary: bin components for the pypi-hatch_fancy_pypi_readme package.
Group: Binaries
Requires: pypi-hatch_fancy_pypi_readme-license = %{version}-%{release}

%description bin
bin components for the pypi-hatch_fancy_pypi_readme package.


%package license
Summary: license components for the pypi-hatch_fancy_pypi_readme package.
Group: Default

%description license
license components for the pypi-hatch_fancy_pypi_readme package.


%package python
Summary: python components for the pypi-hatch_fancy_pypi_readme package.
Group: Default
Requires: pypi-hatch_fancy_pypi_readme-python3 = %{version}-%{release}

%description python
python components for the pypi-hatch_fancy_pypi_readme package.


%package python3
Summary: python3 components for the pypi-hatch_fancy_pypi_readme package.
Group: Default
Requires: python3-core
Provides: pypi(hatch_fancy_pypi_readme)
Requires: pypi(hatchling)

%description python3
python3 components for the pypi-hatch_fancy_pypi_readme package.


%prep
%setup -q -n hatch_fancy_pypi_readme-23.1.0
cd %{_builddir}/hatch_fancy_pypi_readme-23.1.0
pushd ..
cp -a hatch_fancy_pypi_readme-23.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697320311
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hatch_fancy_pypi_readme
cp %{_builddir}/hatch_fancy_pypi_readme-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-hatch_fancy_pypi_readme/fd5e2e6ccd11c0cf3abdefdf45b23b627d15bda6 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hatch-fancy-pypi-readme

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hatch_fancy_pypi_readme/fd5e2e6ccd11c0cf3abdefdf45b23b627d15bda6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
