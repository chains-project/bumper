Here is a possible patch for the failing client code:
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
The change I made is to create a separate variable for the `StringContains` matcher and pass it directly to the `assertThat` method. This way, the correct number of arguments is passed to the `StringContains` constructor.