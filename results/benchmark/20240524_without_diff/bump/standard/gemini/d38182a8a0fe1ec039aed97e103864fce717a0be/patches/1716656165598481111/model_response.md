```java
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.http.async.AsyncSlice(
        new com.artipie.http.async.SliceAsAsync(
            com.artipie.http.Slice.wrap(
                this.request(
                    new com.artipie.http.rq.RequestLine(
                        com.artipie.http.Slice.wrap(action).toString()
                    ),
                    new com.artipie.http.Headers.From(
                        com.artipie.http.Headers.EMPTY
                    ),
                    com.artipie.http.EmptyBody.EMPTY
                )
            )
        )
    );
}
```