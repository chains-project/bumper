Here's a proposed patch for the failing client code:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ),
        new StringContains("Unexpected path")
    );
}
```

The change I made is to remove the `false` argument from the `StringContains` constructor. It seems that the updated library version no longer accepts a `boolean` argument for this constructor. Instead, the constructor now only takes a single `String` argument representing the expected substring.