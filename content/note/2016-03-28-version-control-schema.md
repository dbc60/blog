---
layout: post
title: Version Control Schema
categories: notes
tags: [history,version]
excerpt: This is pulled from the sqlite3 database that is the storage for the Fossil-SCM version control system. I put it here for reference in case I ever wanted to figure out how to keep a history of changes to a project (for example, adding, removing, or deferring features or tasks).
---

```sql
CREATE TABLE blob(
  rid INTEGER PRIMARY KEY,
  rcvid INTEGER,
  size INTEGER,
  uuid TEXT UNIQUE NOT NULL,
  content BLOB,
  CHECK( length(uuid)==40 AND rid>0 )
);

CREATE TABLE delta(
  rid INTEGER PRIMARY KEY,
  srcid INTEGER NOT NULL REFERENCES blob
);

CREATE INDEX delta_i1 ON delta(srcid);

CREATE TABLE rcvfrom(
  rcvid INTEGER PRIMARY KEY,
  uid INTEGER REFERENCES user,
  mtime DATETIME,
  nonce TEXT UNIQUE,
  ipaddr TEXT
);

CREATE TABLE user(
  uid INTEGER PRIMARY KEY,
  login TEXT UNIQUE,
  pw TEXT,
  cap TEXT,
  cookie TEXT,
  ipaddr TEXT,
  cexpire DATETIME,
  info TEXT,
  mtime DATE,
  photo BLOB
);

CREATE TABLE config(
  name TEXT PRIMARY KEY NOT NULL,
  value CLOB,
  mtime DATE,
  CHECK( typeof(name)='text' AND length(name)>=1 )
);

CREATE TABLE shun(
  uuid UNIQUE,
  mtime DATE,
  scom TEXT
);

CREATE TABLE private(rid INTEGER PRIMARY KEY);

CREATE TABLE reportfmt(
   rn INTEGER PRIMARY KEY,
   owner TEXT,
   title TEXT UNIQUE,
   mtime DATE,
   cols TEXT,
   sqlcode TEXT
);

CREATE TABLE concealed(
  hash TEXT PRIMARY KEY,
  mtime DATE,
  content TEXT
);

CREATE TABLE filename(
  fnid INTEGER PRIMARY KEY,
  name TEXT UNIQUE
);

CREATE TABLE mlink(
  mid INTEGER REFERENCES plink(cid),
  fid INTEGER REFERENCES blob,
  pmid INTEGER REFERENCES plink(cid),
  pid INTEGER REFERENCES blob,
  fnid INTEGER REFERENCES filename,
  pfnid INTEGER REFERENCES filename,
  mperm INTEGER,
  isaux BOOLEAN DEFAULT 0
);

CREATE INDEX mlink_i1 ON mlink(mid);

CREATE INDEX mlink_i2 ON mlink(fnid);

CREATE INDEX mlink_i3 ON mlink(fid);

CREATE INDEX mlink_i4 ON mlink(pid);

CREATE TABLE plink(
  pid INTEGER REFERENCES blob,
  cid INTEGER REFERENCES blob,
  isprim BOOLEAN,
  mtime DATETIME,
  baseid INTEGER REFERENCES blob,
  UNIQUE(pid, cid)
);

CREATE INDEX plink_i2 ON plink(cid,pid);

CREATE TABLE leaf(rid INTEGER PRIMARY KEY);

CREATE TABLE event(
  type TEXT,
  mtime DATETIME,
  objid INTEGER PRIMARY KEY,
  tagid INTEGER,
  uid INTEGER REFERENCES user,
  bgcolor TEXT,
  euser TEXT,
  user TEXT,
  ecomment TEXT,
  comment TEXT,
  brief TEXT,
  omtime DATETIME
);

CREATE INDEX event_i1 ON event(mtime);

CREATE TABLE phantom(
  rid INTEGER PRIMARY KEY
);

CREATE TABLE orphan(
  rid INTEGER PRIMARY KEY,
  baseline INTEGER
);

CREATE INDEX orphan_baseline ON orphan(baseline);

CREATE TABLE unclustered(
  rid INTEGER PRIMARY KEY
);

CREATE TABLE unsent(
  rid INTEGER PRIMARY KEY
);

CREATE TABLE tag(
  tagid INTEGER PRIMARY KEY,
  tagname TEXT UNIQUE
);

CREATE TABLE tagxref(
  tagid INTEGER REFERENCES tag,
  tagtype INTEGER,
  srcid INTEGER REFERENCES blob,
  origid INTEGER REFERENCES blob,
  value TEXT,
  mtime TIMESTAMP,
  rid INTEGER REFERENCE blob,
  UNIQUE(rid, tagid)
);

CREATE INDEX tagxref_i1 ON tagxref(tagid, mtime);

CREATE TABLE backlink(
  target TEXT,
  srctype INT,
  srcid INT,
  mtime TIMESTAMP,
  UNIQUE(target, srctype, srcid)
);

CREATE INDEX backlink_src ON backlink(srcid, srctype);

CREATE TABLE attachment(
  attachid INTEGER PRIMARY KEY,
  isLatest BOOLEAN DEFAULT 0,
  mtime TIMESTAMP,
  src TEXT,
  target TEXT,
  filename TEXT,
  comment TEXT,
  user TEXT
);

CREATE INDEX attachment_idx1 ON attachment(target, filename, mtime);

CREATE INDEX attachment_idx2 ON attachment(src);

CREATE TABLE ticket(
  -- Do not change any column that begins with tkt_
  tkt_id INTEGER PRIMARY KEY,
  tkt_uuid TEXT UNIQUE,
  tkt_mtime DATE,
  tkt_ctime DATE,
  -- Add as many fields as required below this line
  type TEXT,
  status TEXT,
  subsystem TEXT,
  priority TEXT,
  severity TEXT,
  foundin TEXT,
  private_contact TEXT,
  resolution TEXT,
  title TEXT,
  comment TEXT
);

CREATE TABLE ticketchng(
  -- Do not change any column that begins with tkt_
  tkt_id INTEGER REFERENCES ticket,
  tkt_rid INTEGER REFERENCES blob,
  tkt_mtime DATE,
  -- Add as many fields as required below this line
  login TEXT,
  username TEXT,
  mimetype TEXT,
  icomment TEXT
);

CREATE INDEX ticketchng_idx1 ON ticketchng(tkt_id, tkt_mtime);
```
