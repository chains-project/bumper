```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    IllegalArgumentException thrown = Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
    );

    MatcherAssert.assertThat(
            thrown.getMessage(),
            CoreMatchers.containsString("Unexpected path")
    );
}
```