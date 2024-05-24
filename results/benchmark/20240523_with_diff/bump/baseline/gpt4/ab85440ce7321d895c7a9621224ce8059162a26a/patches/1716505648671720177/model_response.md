```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    StringContains contains = new StringContains("Unexpected path");
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ).getMessage(),
        contains
    );
}
```