# URLs

* `GET /` shows the last 10 Flutts from most to least recent
* `GET flutz/search?query=QUERY_TEXT` shows the last 10 Flutts containing `QUERY_TEXT` text from most to least recent
* `GET flutz/post` shows a form to submit a Flutts
* `POST flutz/post/` accepts the new flut data and shows the ack page.
* `GET accounts/login` a login page

### TODO:

* Add a `GET /user/USER_ID` route which shows the last 10 Flutts of a given user from most to least recent

