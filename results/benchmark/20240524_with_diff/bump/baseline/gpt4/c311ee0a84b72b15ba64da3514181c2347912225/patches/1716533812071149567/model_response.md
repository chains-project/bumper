```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    Throwable exception = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    );
    MatcherAssert.assertThat(
        exception.getMessage(),
        CoreMatchers.containsString("Unexpected path")
    );
}
```