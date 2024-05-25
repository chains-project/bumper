Here's the proposed patch for the failing client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class TagValidTest {

    private Tag.Valid tag;

    @BeforeEach
    void setUp() {
        tag = new Tag.Valid("");
    }

    @Test
    @ValueSource(strings = {
            "",
            ".0",
            "*",
            "\u00ea",
            "-my-tag",
            "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678"
    })
    void shouldFailToGetValueWhenInvalid(String original) {
        tag = new Tag.Valid(original);
        InvalidTagNameException exception = assertThrows(
                InvalidTagNameException.class,
                tag::value
        );
        assertThat(tag.valid(), new IsEqual<>(false));
        assertThat(exception.getMessage(),
                allOf(
                        containsString("Invalid tag"),
                        not(containsString(original))
                )
        );
    }
}
```

This patch moves the `MatcherAssert.assertThat` call to a separate line, so that the error message can be constructed using `allOf` and `containsString` matchers instead of `StringContains`. This should resolve the compilation error.