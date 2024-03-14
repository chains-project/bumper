```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String expectedMessage = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();
    MatcherAssert.assertThat(
        expectedMessage,
        CoreMatchers.containsString("Unexpected path")
    );
}
```