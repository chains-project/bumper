Here's the proposed patch:

```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
              StringContains matcher = new StringContains("Unexpected query");
              new UploadEntity.Request(
                      new RequestLine(
                              RqMethod.PUT,
                              "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                      ).toString()
                  ).digest();
              return false;
            }
        ),
        matcher
    );
}
```

The changes I made are:

* I created a `matcher` variable to store the `StringContains` matcher, which is used in the `assertThat` method.
* I wrapped the `new UploadEntity.Request` and `digest()` calls in a lambda expression, which returns `false`. This allows us to use the `StringContains` constructor that only takes a single `String` argument.
* I removed the `Override` decorator since it's not necessary in this case.
* I did not use any removed library methods, and I used the added `StringContains` constructor that takes a single `String` argument.