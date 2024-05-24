Here is the proposed patch:
```java
    @Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> {
                    StringContains stringContains = new StringContains("Unexpected query");
                    new UploadEntity.Request(
                        new RequestLine(
                            RqMethod.PUT,
                            "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                        ).toString()
                    ).digest();
                    return null;
                }
            ).getMessage(),
            stringContains
        );
    }
```
The changes made are:

* The `StringContains` constructor is now called with a single argument, as required by the new library version.
* A local variable `stringContains` is created to hold the `StringContains` matcher, which is then passed to `MatcherAssert.assertThat()`.
* An empty block `{}` is added to the lambda expression to satisfy the method's requirement for a `void` return type.
* A `return null;` statement is added to the lambda expression to satisfy the method's requirement for a return value.