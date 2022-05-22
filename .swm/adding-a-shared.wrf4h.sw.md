---
id: wrf4h
name: Adding a Shared
file_version: 1.0.2
app_version: 0.8.6-0
file_blobs:
  venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py: f997e2444e75b176761965bbf3e1f82c5c3ad0e2
  venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py: a6f44a55c6377c746ec8ca831999fdde5e401aa6
  venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/mkdirlockfile.py: 05a8c96ca517271bbd4953d0cf83dc4173521b2e
  venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/linklockfile.py: 2ca9be0423591e61b3382b559473fcc56363cc46
  venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/pidlockfile.py: 069e85b15bdfcb4fd7042222516fbfb046db06c9
---

In this document, we will learn how to add a new dfdShared to the system.

A Shared is {Explain what a Shared is and its role in the system}

In order to add a new Shared, we create a class that inherits from `_SharedBase`[<sup id="Z24fiLo">↓</sup>](#f-Z24fiLo).

Some examples of `_SharedBase`[<sup id="Z24fiLo">↓</sup>](#f-Z24fiLo)s are `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI), `MkdirLockFile`[<sup id="Z2jnekc">↓</sup>](#f-Z2jnekc), `LinkLockFile`[<sup id="M2l7s">↓</sup>](#f-M2l7s), and `PIDLockFile`[<sup id="2a7v6s">↓</sup>](#f-2a7v6s). Note: some of these examples inherit indirectly from `_SharedBase`[<sup id="Z24fiLo">↓</sup>](#f-Z24fiLo).

<br/>

> **NOTE: Inherit from `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI)**
>
> Most `_SharedBase`[<sup id="Z24fiLo">↓</sup>](#f-Z24fiLo)s inherit directly from `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI) and almost none inherit directly from `_SharedBase`[<sup id="Z24fiLo">↓</sup>](#f-Z24fiLo).
> In this document we demonstrate inheriting from `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI).

<br/>

## TL;DR - How to Add a `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI)

1. Create a new class inheriting from `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI)&nbsp;
   - Place the file under [[sym:./venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile({"type":"path","text":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile","path":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile"})]],
     e.g. `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) is defined in [[sym:./venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py({"type":"path","text":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py","path":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py"})]].
2. Implement `acquire`[<sup id="ZrdIAQ">↓</sup>](#f-ZrdIAQ), `break_lock`[<sup id="Z5I6dO">↓</sup>](#f-Z5I6dO), `i_am_locking`[<sup id="Z1DUrfs">↓</sup>](#f-Z1DUrfs), `is_locked`[<sup id="1VvicN">↓</sup>](#f-1VvicN), `release`[<sup id="1goyjJ">↓</sup>](#f-1goyjJ), and `__init__`[<sup id="rR08E">↓</sup>](#f-rR08E).
3. Update [[sym:./venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py({"type":"path","text":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py","path":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py"})]].
4. **Profit** 💰

<br/>

## Example Walkthrough - `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI)
We'll follow the implementation of `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) for this example.

A `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) is {Explain what SQLiteLockFile is and how it works with the Shared interface}

<br/>

## Steps to Adding a new `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI)

<br/>

### 1\. Inherit from `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI).
All `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI)s are defined in files under [[sym:./venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile({"type":"path","text":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile","path":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile"})]].

<br/>

We first need to define our class in the relevant file, and inherit from `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI):
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 11     from . import LockBase, NotLocked, NotMyLock, LockTimeout, AlreadyLocked
⬜ 12     
⬜ 13     
🟩 14     class SQLiteLockFile(LockBase):
⬜ 15         "Demonstrate SQL-based locking."
⬜ 16     
⬜ 17         testdb = None
```

<br/>

> **Note**: the class name should end with "LockFile".

<br/>

### 2\. Implement `acquire`[<sup id="ZrdIAQ">↓</sup>](#f-ZrdIAQ), `break_lock`[<sup id="Z5I6dO">↓</sup>](#f-Z5I6dO), `i_am_locking`[<sup id="Z1DUrfs">↓</sup>](#f-Z1DUrfs), `is_locked`[<sup id="1VvicN">↓</sup>](#f-1VvicN), `release`[<sup id="1goyjJ">↓</sup>](#f-1goyjJ), and `__init__`[<sup id="rR08E">↓</sup>](#f-rR08E)

<br/>

The goal of `acquire`[<sup id="ZrdIAQ">↓</sup>](#f-ZrdIAQ) is to {Explain acquire's role}.

<br/>

This is how we implemented it for `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) {Explain what's happening in this implementation}
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 50                 import atexit
⬜ 51                 atexit.register(os.unlink, SQLiteLockFile.testdb)
⬜ 52     
🟩 53         def acquire(self, timeout=None):
🟩 54             timeout = timeout if timeout is not None else self.timeout
🟩 55             end_time = time.time()
🟩 56             if timeout is not None and timeout > 0:
🟩 57                 end_time += timeout
🟩 58     
🟩 59             if timeout is None:
🟩 60                 wait = 0.1
🟩 61             elif timeout <= 0:
🟩 62                 wait = 0
🟩 63             else:
🟩 64                 wait = timeout / 10
🟩 65     
🟩 66             cursor = self.connection.cursor()
🟩 67     
🟩 68             while True:
🟩 69                 if not self.is_locked():
🟩 70                     # Not locked.  Try to lock it.
🟩 71                     cursor.execute("insert into locks"
🟩 72                                    "  (lock_file, unique_name)"
🟩 73                                    "  values"
🟩 74                                    "  (?, ?)",
🟩 75                                    (self.lock_file, self.unique_name))
🟩 76                     self.connection.commit()
🟩 77     
🟩 78                     # Check to see if we are the only lock holder.
🟩 79                     cursor.execute("select * from locks"
🟩 80                                    "  where unique_name = ?",
🟩 81                                    (self.unique_name,))
🟩 82                     rows = cursor.fetchall()
🟩 83                     if len(rows) > 1:
🟩 84                         # Nope.  Someone else got there.  Remove our lock.
🟩 85                         cursor.execute("delete from locks"
🟩 86                                        "  where unique_name = ?",
🟩 87                                        (self.unique_name,))
🟩 88                         self.connection.commit()
🟩 89                     else:
🟩 90                         # Yup.  We're done, so go home.
🟩 91                         return
🟩 92                 else:
🟩 93                     # Check to see if we are the only lock holder.
⬜ 94                     cursor.execute("select * from locks"
⬜ 95                                    "  where unique_name = ?",
⬜ 96                                    (self.unique_name,))
```

<br/>

The goal of `break_lock`[<sup id="Z5I6dO">↓</sup>](#f-Z5I6dO) is to {Explain break_lock's role}.

<br/>

This is how we implemented it for `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) {Explain what's happening in this implementation}
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 148                           (self.lock_file, self.unique_name))
⬜ 149            return not not cursor.fetchall()
⬜ 150    
🟩 151        def break_lock(self):
🟩 152            cursor = self.connection.cursor()
🟩 153            cursor.execute("delete from locks"
🟩 154                           "  where lock_file = ?",
🟩 155                           (self.lock_file,))
🟩 156            self.connection.commit()
⬜ 157    
```

<br/>

The goal of `i_am_locking`[<sup id="Z1DUrfs">↓</sup>](#f-Z1DUrfs) is to {Explain i_am_locking's role}.

<br/>

This is how we implemented it for `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) {Explain what's happening in this implementation}
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 140            rows = cursor.fetchall()
⬜ 141            return not not rows
⬜ 142    
🟩 143        def i_am_locking(self):
🟩 144            cursor = self.connection.cursor()
🟩 145            cursor.execute("select * from locks"
🟩 146                           "  where lock_file = ?"
🟩 147                           "    and unique_name = ?",
🟩 148                           (self.lock_file, self.unique_name))
🟩 149            return not not cursor.fetchall()
⬜ 150    
⬜ 151        def break_lock(self):
⬜ 152            cursor = self.connection.cursor()
```

<br/>

The goal of `is_locked`[<sup id="1VvicN">↓</sup>](#f-1VvicN) is to {Explain is_locked's role}.

<br/>

This is how we implemented it for `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) {Explain what's happening in this implementation}
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 132                           (self.lock_file,))
⬜ 133            return cursor.fetchone()[0]
⬜ 134    
🟩 135        def is_locked(self):
🟩 136            cursor = self.connection.cursor()
🟩 137            cursor.execute("select * from locks"
🟩 138                           "  where lock_file = ?",
🟩 139                           (self.lock_file,))
🟩 140            rows = cursor.fetchall()
🟩 141            return not not rows
⬜ 142    
⬜ 143        def i_am_locking(self):
⬜ 144            cursor = self.connection.cursor()
```

<br/>

The goal of `release`[<sup id="1goyjJ">↓</sup>](#f-1goyjJ) is to {Explain release's role}.

<br/>

This is how we implemented it for `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) {Explain what's happening in this implementation}
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 113                # Well, okay.  We'll give it a bit longer.
⬜ 114                time.sleep(wait)
⬜ 115    
🟩 116        def release(self):
🟩 117            if not self.is_locked():
🟩 118                raise NotLocked("%s is not locked" % self.path)
🟩 119            if not self.i_am_locking():
🟩 120                raise NotMyLock("%s is locked, but not by me (by %s)" %
🟩 121                                (self.unique_name, self._who_is_locking()))
🟩 122            cursor = self.connection.cursor()
🟩 123            cursor.execute("delete from locks"
🟩 124                           "  where unique_name = ?",
🟩 125                           (self.unique_name,))
🟩 126            self.connection.commit()
⬜ 127    
⬜ 128        def _who_is_locking(self):
⬜ 129            cursor = self.connection.cursor()
```

<br/>

Implement `__init__`[<sup id="rR08E">↓</sup>](#f-rR08E).

<br/>

This is how we implemented it for `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) {Explain what's happening in this implementation}
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py
```python
⬜ 16     
⬜ 17         testdb = None
⬜ 18     
🟩 19         def __init__(self, path, threaded=True, timeout=None):
🟩 20             """
🟩 21             >>> lock = SQLiteLockFile('somefile')
🟩 22             >>> lock = SQLiteLockFile('somefile', threaded=False)
🟩 23             """
🟩 24             LockBase.__init__(self, path, threaded, timeout)
🟩 25             self.lock_file = unicode(self.lock_file)
🟩 26             self.unique_name = unicode(self.unique_name)
🟩 27     
🟩 28             if SQLiteLockFile.testdb is None:
🟩 29                 import tempfile
🟩 30                 _fd, testdb = tempfile.mkstemp()
🟩 31                 os.close(_fd)
🟩 32                 os.unlink(testdb)
🟩 33                 del _fd, tempfile
🟩 34                 SQLiteLockFile.testdb = testdb
🟩 35     
🟩 36             import sqlite3
🟩 37             self.connection = sqlite3.connect(SQLiteLockFile.testdb)
🟩 38     
🟩 39             c = self.connection.cursor()
🟩 40             try:
🟩 41                 c.execute("create table locks"
🟩 42                           "("
🟩 43                           "   lock_file varchar(32),"
🟩 44                           "   unique_name varchar(32)"
🟩 45                           ")")
🟩 46             except sqlite3.OperationalError:
🟩 47                 pass
🟩 48             else:
🟩 49                 self.connection.commit()
🟩 50                 import atexit
🟩 51                 atexit.register(os.unlink, SQLiteLockFile.testdb)
⬜ 52     
⬜ 53         def acquire(self, timeout=None):
⬜ 54             timeout = timeout if timeout is not None else self.timeout
```

<br/>

## Update [[sym:./venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py({"type":"path","text":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py","path":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py"})]]
Every time we add a new `LockBase`[<sup id="2w5LSI">↓</sup>](#f-2w5LSI), we reference it in [[sym:./venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py({"type":"path","text":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py","path":"venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py"})]].
We will still look at `SQLiteLockFile`[<sup id="2nWuFI">↓</sup>](#f-2nWuFI) as our example.

<br/>


<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py
```python
⬜ 304    def SQLiteFileLock(*args, **kwds):
⬜ 305        """Factory function provided for backwards compatibility.
⬜ 306    
🟩 307        Do not use in new code.  Instead, import SQLiteLockFile from the
⬜ 308        lockfile.mkdirlockfile module.
⬜ 309        """
⬜ 310        from . import sqlitelockfile
🟩 311        return _fl_helper(sqlitelockfile.SQLiteLockFile, "lockfile.sqlitelockfile",
⬜ 312                          *args, **kwds)
⬜ 313    
⬜ 314    
```

<br/>

<!-- THIS IS AN AUTOGENERATED SECTION. DO NOT EDIT THIS SECTION DIRECTLY -->
### Swimm Note

<span id="f-rR08E">__init__</span>[^](#rR08E) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L19
```python
    def __init__(self, path, threaded=True, timeout=None):
```

<span id="f-Z24fiLo">_SharedBase</span>[^](#Z24fiLo) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py" L165
```python
class _SharedBase(object):
```

<span id="f-ZrdIAQ">acquire</span>[^](#ZrdIAQ) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L53
```python
    def acquire(self, timeout=None):
```

<span id="f-Z5I6dO">break_lock</span>[^](#Z5I6dO) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L151
```python
    def break_lock(self):
```

<span id="f-Z1DUrfs">i_am_locking</span>[^](#Z1DUrfs) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L143
```python
    def i_am_locking(self):
```

<span id="f-1VvicN">is_locked</span>[^](#1VvicN) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L135
```python
    def is_locked(self):
```

<span id="f-M2l7s">LinkLockFile</span>[^](#M2l7s) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/linklockfile.py" L10
```python
class LinkLockFile(LockBase):
```

<span id="f-2w5LSI">LockBase</span>[^](#2w5LSI) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/__init__.py" L210
```python
class LockBase(_SharedBase):
```

<span id="f-Z2jnekc">MkdirLockFile</span>[^](#Z2jnekc) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/mkdirlockfile.py" L12
```python
class MkdirLockFile(LockBase):
```

<span id="f-2a7v6s">PIDLockFile</span>[^](#2a7v6s) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/pidlockfile.py" L25
```python
class PIDLockFile(LockBase):
```

<span id="f-1goyjJ">release</span>[^](#1goyjJ) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L116
```python
    def release(self):
```

<span id="f-2nWuFI">SQLiteLockFile</span>[^](#2nWuFI) - "venv/Lib/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/lockfile/sqlitelockfile.py" L14
```python
class SQLiteLockFile(LockBase):
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://swimm-web-app.web.app/repos/Z2l0aHViJTNBJTNBZGlnaS1wcm9qLUdVSSUzQSUzQWdpbGFkYXg=/docs/wrf4h).