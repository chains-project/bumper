```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String expectedMessage = "Unexpected path";
    Throwable thrown = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    );
    MatcherAssert.assertThat(thrown.getMessage(), Matchers.containsString(expectedMessage));
}
```