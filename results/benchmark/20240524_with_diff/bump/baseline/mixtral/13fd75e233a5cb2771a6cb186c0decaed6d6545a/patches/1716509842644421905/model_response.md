Here is the proposed patch:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    StringContains stringContains = new StringContains("Unexpected path");
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ).getMessage(),
        stringContains
    );
}
```

The only change made is to create a separate variable for the `StringContains` matcher, which resolves the error message.