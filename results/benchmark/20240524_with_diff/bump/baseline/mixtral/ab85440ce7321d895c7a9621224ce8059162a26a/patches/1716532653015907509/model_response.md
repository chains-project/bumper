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
        new StringStartsWith("Unexpected path")
    );
}
```

In the new version of the library, the `StringContains` constructor has been changed to accept only one argument. Therefore, I replaced it with the `StringStartsWith` matcher, which checks if a string starts with a given substring.