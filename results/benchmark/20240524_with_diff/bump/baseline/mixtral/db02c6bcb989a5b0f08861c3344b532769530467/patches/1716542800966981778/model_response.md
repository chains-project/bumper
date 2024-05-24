Here is a possible patch for the failing client code:

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

In this patch, I have removed the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor with a `boolean` argument was removed in the new library version, and the constructor with a single `String` argument is still available. This should fix the error message you provided.