create table status(
  id integer NOT NULL,
  text text NOT NULL,
  in_reply_to_status_id integer default 0,
  user_id integer NOT NULL,
  is_quote_status integer NOT NULL,
  created_at integer NOT NULL,
  CONSTRAINT status_id PRIMARY KEY (id)
);

create table conversation(
  sid1 integer NOT NULL,
  sid2 integer NOT NULL,
  sid3 integer NOT NULL,
  CONSTRAINT converstaion_id PRIMARY KEY (sid1, sid2, sid3)
);
