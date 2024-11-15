```java
import com.jcabi.aspects.Tv;
  import com.jcabi.jdbc.JdbcSession;
  import com.jcabi.jdbc.SingleOutcome;
  import com.jcabi.jdbc.Table;
  import com.jcabi.jdbc.Value;
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.SQLException;
  import java.sql.Statement;
  import java.util.ArrayList;
  import java.util.Arrays;
  import java.util.List;
  import org.junit.After;
  import org.junit.Before;
  import org.junit.Test;

  public abstract class RegionITCase {
    private static final String JDBC_URL = "jdbc:h2:mem:test";
    private static final String JDBC_USER = "sa";
    private static final String JDBC_PASS = "";
    private static final String JDBC_DRIVER = "org.h2.Driver";
    private static final String[] SQL = new String[] {
        "CREATE TABLE regions (id INT PRIMARY KEY, name VARCHAR(255))",
        "INSERT INTO regions (id, name) VALUES (1, 'Region 1')",
        "INSERT INTO regions (id, name) VALUES (2, 'Region 2')",
        "INSERT INTO regions (id, name) VALUES (3, 'Region 3')"
    };
    private Connection connection;
    private Statement statement;
    private JdbcSession session;
    private Table table;

    @Before
    public void setUp() throws SQLException {
      Class.forName(JDBC_DRIVER);
      connection = DriverManager.getConnection(JDBC_URL, JDBC_USER, JDBC_PASS);
      statement = connection.createStatement();
      for (String sql : SQL) {
        statement.executeUpdate(sql);
      }
      session = new JdbcSession(connection);
      table = session.table("regions");
    }

    @After
    public void tearDown() throws SQLException {
      statement.close();
      connection.close();
    }

    @Test
    public void testInsert() throws SQLException {
      table.insert(new Value("name").set("Region 4"));
      Tv.debug("Inserted");
    }

    @Test
    public void testUpdate() throws SQLException {
      table.update(new Value("name").set("Region 4"), new Value("id").set(1));
      Tv.debug("Updated");
    }

    @Test
    public void testDelete() throws SQLException {
      table.delete(new Value("id").set(1));
      Tv.debug("Deleted");
    }

    @Test
    public void testSelect() throws SQLException {
      List<String> names = new ArrayList<String>();
      for (Value row : table.select(new Value("name"))) {
        names.add(row.get("name"));
      }
      Tv.debug("Names: %s", names);
      assert names.equals(Arrays.asList("Region 1", "Region 2", "Region 3"));
    }

    @Test
    public void testSingle() throws SQLException {
      String name = new SingleOutcome<String>(table.select(
          new Value("name"),
          new Value("id").set(1)
      )).value();
      Tv.debug("Name: %s", name);
      assert name.equals("Region 1");
    }
  }
```