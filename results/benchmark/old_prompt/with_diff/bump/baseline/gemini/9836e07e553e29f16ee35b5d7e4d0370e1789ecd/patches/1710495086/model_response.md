```java
void shouldFailToGetValueWhenInvalid(final String original) {
        final Tag.Valid tag = new Tag.Valid(original);
        MatcherAssert.assertThat(tag.valid(), IsEqual.equalTo(false));
        final Throwable throwable = Assertions.assertThrows(
            InvalidTagNameException.class,
            tag::value
        );
        MatcherAssert.assertThat(
            throwable.getMessage(),
            AllOf.allOf(
                Arrays.asList(
                    new StringContains(true, "Invalid tag"),
                    new StringContains(false, original)
                )
            )
        );
    }
```