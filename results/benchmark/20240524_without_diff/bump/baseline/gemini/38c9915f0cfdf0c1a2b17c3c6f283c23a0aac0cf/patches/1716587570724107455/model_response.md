```java
  import org.cactoos.iterable.LengthOf;

  public class RtTransaction {
    public static final String ID = "id";
    public static final String HASH = "hash";
    public static final String PARENT_HASH = "parentHash";
    public static final String TIMESTAMP = "timestamp";
    public static final String FEE = "fee";
    public static final String SENDER = "sender";
    public static final String RECIPIENT = "recipient";
    public static final String AMOUNT = "amount";
    public static final String DATA = "data";
    public static final String SIGNATURE = "signature";
    public static final String HEIGHT = "height";
    public static final String DIFFICULTY = "difficulty";
    public static final String SIZE = "size";
    public static final String WEIGHT = "weight";
    public static final String VERSION = "version";
    public static final String BLOCK_HASH = "blockHash";
    public static final String CONFIRMATIONS = "confirmations";
    public static final String TIME = "time";
    public static final String BLOCK_TIME = "blockTime";
    public static final String INDEX = "index";
    public static final String MEMPOOL = "mempool";
    public static final String RAW = "raw";
    public static final String VIN = "vin";
    public static final String VOUT = "vout";
    public static final String COINBASE = "coinbase";
    public static final String TXID = "txid";
    public static final String VALUE = "value";
    public static final String N = "n";
    public static final String SCRIPT_SIG = "scriptSig";
    public static final String SEQUENCE = "sequence";
    public static final String ADDR = "addr";
    public static final String VALUE_SAT = "valueSat";
    public static final String DOUBLE_SPEND = "doubleSpend";
    public static final String ASSEMBLIES = "assemblies";
    public static final String DETAILS = "details";
    public static final String HEX = "hex";
    public static final String ASM = "asm";
    public static final String TYPE = "type";
    public static final String SPENT = "spent";
    public static final String SPENDABLE = "spendable";
    public static final String CONFIRMED = "confirmed";
    public static final String LOCKTIME = "locktime";
    public static final String EXPIRY_HEIGHT = "expiryHeight";
    public static final String VALUE_ZAT = "valueZat";

    private final String id;
    private final String hash;
    private final String parentHash;
    private final Long timestamp;
    private final Long fee;
    private final String sender;
    private final String recipient;
    private final Long amount;
    private final String data;
    private final String signature;
    private final Long height;
    private final Long difficulty;
    private final Long size;
    private final Long weight;
    private final Long version;
    private final String blockHash;
    private final Long confirmations;
    private final Long time;
    private final Long blockTime;
    private final Long index;
    private final Boolean mempool;
    private final String raw;
    private final List<Vin> vin;
    private final List<Vout> vout;
    private final Boolean coinbase;
    private final String txid;
    private final Long value;
    private final Long n;
    private final String scriptSig;
    private final Long sequence;
    private final String addr;
    private final Long valueSat;
    private final Boolean doubleSpend;
    private final List<Assembly> assemblies;
    private final List<Detail> details;
    private final String hex;
    private final String asm;
    private final String type;
    private final Boolean spent;
    private final Boolean spendable;
    private final Boolean confirmed;
    private final Long locktime;
    private final Long expiryHeight;
    private final Long valueZat;

    public RtTransaction(
        final String id,
        final String hash,
        final String parentHash,
        final Long timestamp,
        final Long fee,
        final String sender,
        final String recipient,
        final Long amount,
        final String data,
        final String signature,
        final Long height,
        final Long difficulty,
        final Long size,
        final Long weight,
        final Long version,
        final String blockHash,
        final Long confirmations,
        final Long time,
        final Long blockTime,
        final Long index,
        final Boolean mempool,
        final String raw,
        final List<Vin> vin,
        final List<Vout> vout,
        final Boolean coinbase,
        final String txid,
        final Long value,
        final Long n,
        final String scriptSig,
        final Long sequence,
        final String addr,
        final Long valueSat,
        final Boolean doubleSpend,
        final List<Assembly> assemblies,
        final List<Detail> details,
        final String hex,
        final String asm,
        final String type,
        final Boolean spent,
        final Boolean spendable,
        final Boolean confirmed,
        final Long locktime,
        final Long expiryHeight,
        final Long valueZat
    ) {
      this.id = id;
      this.hash = hash;
      this.parentHash = parentHash;
      this.timestamp = timestamp;
      this.fee = fee;
      this.sender = sender;
      this.recipient = recipient;
      this.amount = amount;
      this.data = data;
      this.signature = signature;
      this.height = height;
      this.difficulty = difficulty;
      this.size = size;
      this.weight = weight;
      this.version = version;
      this.blockHash = blockHash;
      this.confirmations = confirmations;
      this.time = time;
      this.blockTime = blockTime;
      this.index = index;
      this.mempool = mempool;
      this.raw = raw;
      this.vin = vin;
      this.vout = vout;
      this.coinbase = coinbase;
      this.txid = txid;
      this.value = value;
      this.n = n;
      this.scriptSig = scriptSig;
      this.sequence = sequence;
      this.addr = addr;
      this.valueSat = valueSat;
      this.doubleSpend = doubleSpend;
      this.assemblies = assemblies;
      this.details = details;
      this.hex = hex;
      this.asm = asm;
      this.type = type;
      this.spent = spent;
      this.spendable = spendable;
      this.confirmed = confirmed;
      this.locktime = locktime;
      this.expiryHeight = expiryHeight;
      this.valueZat = valueZat;
    }

    public String id() {
      return id;
    }

    public String hash() {
      return hash;
    }

    public String parentHash() {
      return parentHash;
    }

    public Long timestamp() {
      return timestamp;
    }

    public Long fee() {
      return fee;
    }

    public String sender() {
      return sender;
    }

    public String recipient() {
      return recipient;
    }

    public Long amount() {
      return amount;
    }

    public String data() {
      return data;
    }

    public String signature() {
      return signature;
    }

    public Long height() {
      return height;
    }

    public Long difficulty() {
      return difficulty;
    }

    public Long size() {
      return size;
    }

    public Long weight() {
      return weight;
    }

    public Long version() {
      return version;
    }

    public String blockHash() {
      return blockHash;
    }

    public Long confirmations() {
      return confirmations;
    }

    public Long time() {
      return time;
    }

    public Long blockTime() {
      return blockTime;
    }

    public Long index() {
      return index;
    }

    public Boolean mempool() {
      return mempool;
    }

    public String raw() {
      return raw;
    }

    public List<Vin> vin() {
      return vin;
    }

    public List<Vout> vout() {
      return vout;
    }

    public Boolean coinbase() {
      return coinbase;
    }

    public String txid() {
      return txid;
    }

    public Long value() {
      return value;
    }

    public Long n() {
      return n;
    }

    public String scriptSig() {
      return scriptSig;
    }

    public Long sequence() {
      return sequence;
    }

    public String addr() {
      return addr;
    }

    public Long valueSat() {
      return valueSat;
    }

    public Boolean doubleSpend() {
      return doubleSpend;
    }

    public List<Assembly> assemblies() {
      return assemblies;
    }

    public List<Detail> details() {
      return details;
    }

    public String hex() {
      return hex;
    }

    public String asm() {
      return asm;
    }

    public String type() {
      return type;
    }

    public Boolean spent() {
      return spent;
    }

    public Boolean spendable() {
      return spendable;
    }

    public Boolean confirmed() {
      return confirmed;
    }

    public Long locktime() {
      return locktime;
    }

    public Long expiryHeight() {
      return expiryHeight;
    }

    public Long valueZat() {
      return valueZat;
    }

    public static RtTransaction from(final Map<String, Object> map) {
      final String id = (String) map.get(ID);
      final String hash = (String) map.get(HASH);
      final String parentHash = (String) map.get(PARENT_HASH);
      final Long timestamp = (Long) map.get(TIMESTAMP);
      final Long fee = (Long) map.get(FEE);
      final String sender = (String) map.get(SENDER);
      final String recipient = (String) map.get(RECIPIENT);
      final Long amount = (Long) map.get(AMOUNT);
      final String data = (String) map.get(DATA);
      final String signature = (String) map.get(SIGNATURE);
      final Long height = (Long) map.get(HEIGHT);
      final Long difficulty = (Long) map.get(DIFFICULTY);
      final Long size = (Long) map.get(SIZE);
      final Long weight = (Long) map.get(WEIGHT);
      final Long version = (Long) map.get(VERSION);
      final String blockHash = (String) map.get(BLOCK_HASH);
      final Long confirmations = (Long) map.get(CONFIRMATIONS);
      final Long time = (Long) map.get(TIME);
      final Long blockTime = (Long) map.get(BLOCK_TIME);
      final Long index = (Long) map.get(INDEX);
      final Boolean mempool = (Boolean) map.get(MEMPOOL);
      final String raw = (String) map.get(RAW);
      final List<Vin> vin = (List<Vin>) map.get(VIN);
      final List<Vout> vout = (List<Vout>) map.get(VOUT);
      final Boolean coinbase = (Boolean) map.get(COINBASE);
      final String txid = (String) map.get(TXID);
      final Long value = (Long) map.get(VALUE);
      final Long n = (Long) map.get(N);
      final String scriptSig = (String) map.get(SCRIPT_SIG);
      final Long sequence = (Long) map.get(SEQUENCE);
      final String addr = (String) map.get(ADDR);
      final Long valueSat = (Long) map.get(VALUE_SAT);
      final Boolean doubleSpend = (Boolean) map.get(DOUBLE_SPEND);
      final List<Assembly> assemblies = (List<Assembly>) map.get(ASSEMBLIES);
      final List<Detail> details = (List<Detail>) map.get(DETAILS);
      final String hex = (String) map.get(HEX);
      final String asm = (String) map.get(ASM);
      final String type = (String) map.get(TYPE);
      final Boolean spent = (Boolean) map.get(SPENT);
      final Boolean spendable = (Boolean) map.get(SPENDABLE);
      final Boolean confirmed = (Boolean) map.get(CONFIRMED);
      final Long locktime = (Long) map.get(LOCKTIME);
      final Long expiryHeight = (Long) map.get(EXPIRY_HEIGHT);
      final Long valueZat = (Long) map.get(VALUE_ZAT);
      return new RtTransaction(
          id,
          hash,
          parentHash,
          timestamp,
          fee,
          sender,
          recipient,
          amount,
          data,
          signature,
          height,
          difficulty,
          size,
          weight,
          version,
          blockHash,
          confirmations,
          time,
          blockTime,
          index,
          mempool,
          raw,
          vin,
          vout,
          coinbase,
          txid,
          value,
          n,
          scriptSig,
          sequence,
          addr,
          valueSat,
          doubleSpend,
          assemblies,
          details,
          hex,
          asm,
          type,
          spent,
          spendable,
          confirmed,
          locktime,
          expiryHeight,
          valueZat
      );
    }

    public static class Vin {
      private final String txid;
      private final Long vout;
      private final Long sequence;
      private final String n;
      private final String scriptSig;
      private final List<String> addresses;
      private final Long valueSat;
      private final Long valueZat;

      public Vin(
          final String txid,
          final Long vout,
          final Long sequence,
          final String n,
          final String scriptSig,
          final List<String> addresses,
          final Long valueSat,
          final Long valueZat
      ) {
        this.txid = txid;
        this.vout = vout;
        this.sequence = sequence;
        this.n = n;
        this.scriptSig = scriptSig;
        this.addresses = addresses;
        this.valueSat = valueSat;
        this.valueZat = valueZat;
      }

      public String txid() {
        return txid;
      }

      public Long vout() {
        return vout;
      }

      public Long sequence() {
        return sequence;
      }

      public String n() {
        return n;
      }

      public String scriptSig() {
        return scriptSig;
      }

      public List<String> addresses() {
        return addresses;
      }

      public Long valueSat() {
        return valueSat;
      }

      public Long valueZat() {
        return valueZat;
      }
    }

    public static class Vout {
      private final Long value;
      private final Long n;
      private final String scriptPubKey;
      private final List<String> addresses;
      private final Boolean spent;
      private final Boolean spendable;
      private final Long valueSat;
      private final Long valueZat;

      public Vout(
          final Long value,
          final Long n,
          final String scriptPubKey,
          final List<String> addresses,
          final Boolean spent,
          final Boolean spendable,
          final Long valueSat,
          final Long valueZat
      ) {
        this.value = value;
        this.n = n;
        this.scriptPubKey = scriptPubKey;
        this.addresses = addresses;
        this.spent = spent;
        this.spendable = spendable;
        this.valueSat = valueSat;
        this.valueZat = valueZat;
      }

      public Long value() {
        return value;
      }

      public Long n() {
        return n;
      }

      public String scriptPubKey() {
        return scriptPubKey;
      }

      public List<String> addresses() {
        return addresses;
      }

      public Boolean spent() {
        return spent;
      }

      public Boolean spendable() {
        return spendable;
      }

      public Long valueSat() {
        return valueSat;
      }

      public Long valueZat() {
        return valueZat;
      }
    }

    public static class Assembly {
      private final String asm;
      private final String hex;
      private final String type;

      public Assembly(
          final String asm,
          final String hex,
          final String type
      ) {
        this.asm = asm;
        this.hex = hex;
        this.type = type;
      }

      public String asm() {
        return asm;
      }

      public String hex() {
        return hex;
      }

      public String type() {
        return type;
      }
    }

    public static class Detail {
      private final String asm;
      private final String hex;
      private final String type;

      public Detail(
          final String asm,
          final String hex,
          final String type
      ) {
        this.asm = asm;
        this.hex = hex;
        this.type = type;
      }

      public String asm() {
        return asm;
      }

      public String hex() {
        return hex;
      }

      public String type() {
        return type;
      }
    }
  }
```