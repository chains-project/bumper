```java
  @Test
    void shouldThrowExceptionOnInvalidPath() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalArgumentException.class,
                () -> new UploadEntity.Request(
                    new RequestLine(RqMethod.PUT, "/one/two")
                ).name()
            ).getMessage(),
            new StringContains(false, "Unexpected path")
        );
    }
```