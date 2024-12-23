```java
  import org.cactoos.scalar.SolidScalar;
  import org.cactoos.text.TextOf;
  import org.cactoos.list.ListOf;
  import org.cactoos.collection.ScalarWithId;
  import org.cactoos.scalar.LengthOf;
  import org.cactoos.list.ListOfString;
  import org.cactoos.text.FormattedText;
  import org.cactoos.list.ListOfAny;
  import org.cactoos.text.UncheckedText;
  import org.cactoos.list.ListOfScalar;
  import org.cactoos.text.TextOf;
  import org.cactoos.list.ListOf;
  import org.cactoos.collection.ScalarWithId;
  import org.cactoos.scalar.LengthOf;
  import org.cactoos.list.ListOfString;
  import org.cactoos.text.FormattedText;
  import org.cactoos.list.ListOfAny;
  import org.cactoos.text.UncheckedText;
  import org.cactoos.list.ListOfScalar;
  import org.cactoos.text.TextOf;

  import java.util.List;
  import java.util.ArrayList;
  import java.util.Collections;
  import java.util.Map;
  import java.util.HashMap;
  import java.util.Set;
  import java.util.HashSet;
  import java.util.Optional;
  import java.util.stream.Collectors;
  import java.util.stream.Stream;

  import static org.cactoos.list.ListOfAny.of;
  import static org.cactoos.list.ListOfScalar.list;
  import static org.cactoos.list.ListOfString.of;
  import static org.cactoos.text.FormattedText.formatted;
  import static org.cactoos.text.UncheckedText.textOf;

  public class WalletsIn {

    private final List<String> wallets;

    public WalletsIn(final List<String> wallets) {
      this.wallets = wallets;
    }

    public String toCql() {
      final List<String> walletsIn = new ArrayList<>();
      for (final String wallet : this.wallets) {
        walletsIn.add(formatted("'%s'", wallet).asString());
      }
      return formatted("wallet_id IN (%s)", String.join(",", walletsIn)).asString();
    }

    public String toSql() {
      final List<String> walletsIn = new ArrayList<>();
      for (final String wallet : this.wallets) {
        walletsIn.add(formatted("'%s'", wallet).asString());
      }
      return formatted("wallet_id IN (%s)", String.join(",", walletsIn)).asString();
    }
  }
```