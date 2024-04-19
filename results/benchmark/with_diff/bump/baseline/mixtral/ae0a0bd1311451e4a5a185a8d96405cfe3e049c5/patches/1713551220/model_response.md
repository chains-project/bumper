Here's the fixed version of the failing method:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ).getMessage(),
        new StringContains("Unexpected path")
    );
}
```

The issue was caused by passing two arguments to the `StringContains` constructor instead of one. I simply removed the `false` argument, leaving only the expected substring.