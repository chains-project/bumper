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
                return false;
            }
        ).getMessage(),
        stringContains
    );
}
```

The changes made are:

* Create a variable `stringContains` to store the `StringContains` matcher, so that it can be reused.
* Move the creation of the `StringContains` matcher outside of the `assertThat` method call.
* Use a lambda expression with a block body to wrap the code that throws an exception, so that the matcher can be used in the `assertThat` method call.
* Return `false` from the lambda expression, since the `assertThrows` method expects a `Supplier` that returns a value.
* Use the `stringContains` variable in the `assertThat` method call.