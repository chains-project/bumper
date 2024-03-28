```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String errorMessage = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();

    MatcherAssert.assertThat(
        errorMessage,
        CoreMatchers.containsString("Unexpected path")
    );
}
```