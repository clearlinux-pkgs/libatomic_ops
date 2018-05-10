#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libatomic_ops
Version  : 7.4.10
Release  : 20
URL      : https://github.com/ivmai/libatomic_ops/releases/download/v7.4.10/libatomic_ops-7.4.10.tar.gz
Source0  : https://github.com/ivmai/libatomic_ops/releases/download/v7.4.10/libatomic_ops-7.4.10.tar.gz
Summary  : Atomic memory update operations portable implementation
Group    : Development/Tools
License  : GPL-2.0
Requires: libatomic_ops-doc

%description
There are two kinds of entities in this directory:
- Subdirectories corresponding to specific compilers (or compiler/OS combinations).
Each of these includes one or more architecture-specific headers.

%package dev
Summary: dev components for the libatomic_ops package.
Group: Development
Provides: libatomic_ops-devel

%description dev
dev components for the libatomic_ops package.


%package doc
Summary: doc components for the libatomic_ops package.
Group: Documentation

%description doc
doc components for the libatomic_ops package.


%prep
%setup -q -n libatomic_ops-7.4.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513977886
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513977886
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/atomic_ops/ao_version.h
/usr/include/atomic_ops/generalize-arithm.h
/usr/include/atomic_ops/generalize-small.h
/usr/include/atomic_ops/generalize.h
/usr/include/atomic_ops/sysdeps/all_acquire_release_volatile.h
/usr/include/atomic_ops/sysdeps/all_aligned_atomic_load_store.h
/usr/include/atomic_ops/sysdeps/all_atomic_load_store.h
/usr/include/atomic_ops/sysdeps/all_atomic_only_load.h
/usr/include/atomic_ops/sysdeps/ao_t_is_int.h
/usr/include/atomic_ops/sysdeps/armcc/arm_v6.h
/usr/include/atomic_ops/sysdeps/emul_cas.h
/usr/include/atomic_ops/sysdeps/gcc/aarch64.h
/usr/include/atomic_ops/sysdeps/gcc/alpha.h
/usr/include/atomic_ops/sysdeps/gcc/arm.h
/usr/include/atomic_ops/sysdeps/gcc/avr32.h
/usr/include/atomic_ops/sysdeps/gcc/cris.h
/usr/include/atomic_ops/sysdeps/gcc/generic-arithm.h
/usr/include/atomic_ops/sysdeps/gcc/generic-small.h
/usr/include/atomic_ops/sysdeps/gcc/generic.h
/usr/include/atomic_ops/sysdeps/gcc/hexagon.h
/usr/include/atomic_ops/sysdeps/gcc/hppa.h
/usr/include/atomic_ops/sysdeps/gcc/ia64.h
/usr/include/atomic_ops/sysdeps/gcc/m68k.h
/usr/include/atomic_ops/sysdeps/gcc/mips.h
/usr/include/atomic_ops/sysdeps/gcc/powerpc.h
/usr/include/atomic_ops/sysdeps/gcc/s390.h
/usr/include/atomic_ops/sysdeps/gcc/sh.h
/usr/include/atomic_ops/sysdeps/gcc/sparc.h
/usr/include/atomic_ops/sysdeps/gcc/x86.h
/usr/include/atomic_ops/sysdeps/generic_pthread.h
/usr/include/atomic_ops/sysdeps/hpc/hppa.h
/usr/include/atomic_ops/sysdeps/hpc/ia64.h
/usr/include/atomic_ops/sysdeps/ibmc/powerpc.h
/usr/include/atomic_ops/sysdeps/icc/ia64.h
/usr/include/atomic_ops/sysdeps/loadstore/acquire_release_volatile.h
/usr/include/atomic_ops/sysdeps/loadstore/atomic_load.h
/usr/include/atomic_ops/sysdeps/loadstore/atomic_store.h
/usr/include/atomic_ops/sysdeps/loadstore/char_acquire_release_volatile.h
/usr/include/atomic_ops/sysdeps/loadstore/char_atomic_load.h
/usr/include/atomic_ops/sysdeps/loadstore/char_atomic_store.h
/usr/include/atomic_ops/sysdeps/loadstore/double_atomic_load_store.h
/usr/include/atomic_ops/sysdeps/loadstore/int_acquire_release_volatile.h
/usr/include/atomic_ops/sysdeps/loadstore/int_atomic_load.h
/usr/include/atomic_ops/sysdeps/loadstore/int_atomic_store.h
/usr/include/atomic_ops/sysdeps/loadstore/ordered_loads_only.h
/usr/include/atomic_ops/sysdeps/loadstore/ordered_stores_only.h
/usr/include/atomic_ops/sysdeps/loadstore/short_acquire_release_volatile.h
/usr/include/atomic_ops/sysdeps/loadstore/short_atomic_load.h
/usr/include/atomic_ops/sysdeps/loadstore/short_atomic_store.h
/usr/include/atomic_ops/sysdeps/msftc/arm.h
/usr/include/atomic_ops/sysdeps/msftc/common32_defs.h
/usr/include/atomic_ops/sysdeps/msftc/x86.h
/usr/include/atomic_ops/sysdeps/msftc/x86_64.h
/usr/include/atomic_ops/sysdeps/ordered.h
/usr/include/atomic_ops/sysdeps/ordered_except_wr.h
/usr/include/atomic_ops/sysdeps/read_ordered.h
/usr/include/atomic_ops/sysdeps/standard_ao_double_t.h
/usr/include/atomic_ops/sysdeps/sunc/sparc.h
/usr/include/atomic_ops/sysdeps/sunc/x86.h
/usr/include/atomic_ops/sysdeps/test_and_set_t_is_ao_t.h
/usr/include/atomic_ops/sysdeps/test_and_set_t_is_char.h
/usr/lib64/*.a
/usr/lib64/pkgconfig/atomic_ops.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libatomic_ops/*
