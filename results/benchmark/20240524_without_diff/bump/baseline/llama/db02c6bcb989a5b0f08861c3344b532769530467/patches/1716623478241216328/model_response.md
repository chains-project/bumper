```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String expectedMessage = "Unexpected path";
    Throwable exception = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    );
    MatcherAssert.assertThat(exception.getMessage(), CoreMatchers.containsString(expectedMessage));
}
```