```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    final String expectedMessage = "Unexpected path";
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ).getMessage(),
        CoreMatchers.containsString(expectedMessage)
    );
}
```