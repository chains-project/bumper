```java
  import org.cactoos.text.TextOf;
  import java.util.List;
  import java.util.ArrayList;
  import java.util.Arrays;
  import java.util.Collections;
  import java.util.stream.Collectors;

  public class RtTransaction {

    public static List<String> getTransactionOutputs(String txid) {
      List<String> outputs = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawtx/%s", txid);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("out:")) {
            String[] parts = line.split(" ");
            String address = parts[1];
            String value = parts[2];
            outputs.add(String.format("%s:%s", address, value));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return outputs;
    }

    public static List<String> getTransactionInputs(String txid) {
      List<String> inputs = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawtx/%s", txid);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("in:")) {
            String[] parts = line.split(" ");
            String address = parts[1];
            String value = parts[2];
            inputs.add(String.format("%s:%s", address, value));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return inputs;
    }

    public static List<String> getTransactionDetails(String txid) {
      List<String> details = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawtx/%s", txid);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("hash:")) {
            details.add(line.substring(6));
          } else if (line.startsWith("ver:")) {
            details.add(line.substring(4));
          } else if (line.startsWith("vin_sz:")) {
            details.add(line.substring(7));
          } else if (line.startsWith("vout_sz:")) {
            details.add(line.substring(8));
          } else if (line.startsWith("lock_time:")) {
            details.add(line.substring(11));
          } else if (line.startsWith("size:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("block_height:")) {
            details.add(line.substring(13));
          } else if (line.startsWith("time:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("relayed_by:")) {
            details.add(line.substring(11));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return details;
    }

    public static List<String> getBlockTransactions(String blockHash) {
      List<String> transactions = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawblock/%s", blockHash);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("tx:")) {
            transactions.add(line.substring(3));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return transactions;
    }

    public static List<String> getBlockDetails(String blockHash) {
      List<String> details = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawblock/%s", blockHash);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("hash:")) {
            details.add(line.substring(6));
          } else if (line.startsWith("ver:")) {
            details.add(line.substring(4));
          } else if (line.startsWith("prev_block:")) {
            details.add(line.substring(11));
          } else if (line.startsWith("mrkl_root:")) {
            details.add(line.substring(10));
          } else if (line.startsWith("time:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("bits:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("nonce:")) {
            details.add(line.substring(6));
          } else if (line.startsWith("n_tx:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("size:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("block_index:")) {
            details.add(line.substring(12));
          } else if (line.startsWith("main_chain:")) {
            details.add(line.substring(11));
          } else if (line.startsWith("height:")) {
            details.add(line.substring(7));
          } else if (line.startsWith("received_time:")) {
            details.add(line.substring(14));
          } else if (line.startsWith("relayed_by:")) {
            details.add(line.substring(11));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return details;
    }

    public static List<String> getWalletTransactions(String walletAddress) {
      List<String> transactions = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawaddr/%s", walletAddress);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("tx:")) {
            transactions.add(line.substring(3));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return transactions;
    }

    public static List<String> getWalletDetails(String walletAddress) {
      List<String> details = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/rawaddr/%s", walletAddress);
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("hash160:")) {
            details.add(line.substring(9));
          } else if (line.startsWith("address:")) {
            details.add(line.substring(8));
          } else if (line.startsWith("n_tx:")) {
            details.add(line.substring(5));
          } else if (line.startsWith("total_received:")) {
            details.add(line.substring(15));
          } else if (line.startsWith("total_sent:")) {
            details.add(line.substring(11));
          } else if (line.startsWith("final_balance:")) {
            details.add(line.substring(14));
          } else if (line.startsWith("txs:")) {
            details.add(line.substring(4));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return details;
    }

    public static List<String> getBalance(String walletAddress) {
      List<String> balance = new ArrayList<>();
      try {
        String url = String.format("https://blockchain.info/q/addressbalance/%s", walletAddress);
        String response = new TextOf(new Net(url)).asString();
        balance.add(response);
      } catch (Exception e) {
        e.printStackTrace();
      }
      return balance;
    }

    public static List<String> getUnconfirmedTransactions() {
      List<String> transactions = new ArrayList<>();
      try {
        String url = "https://blockchain.info/unconfirmed-transactions?format=json";
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("tx:")) {
            transactions.add(line.substring(3));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return transactions;
    }

    public static List<String> getLatestBlock() {
      List<String> block = new ArrayList<>();
      try {
        String url = "https://blockchain.info/latestblock";
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("hash:")) {
            block.add(line.substring(6));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return block;
    }

    public static List<String> getDifficulty() {
      List<String> difficulty = new ArrayList<>();
      try {
        String url = "https://blockchain.info/q/getdifficulty";
        String response = new TextOf(new Net(url)).asString();
        difficulty.add(response);
      } catch (Exception e) {
        e.printStackTrace();
      }
      return difficulty;
    }

    public static List<String> getBlockHeight() {
      List<String> height = new ArrayList<>();
      try {
        String url = "https://blockchain.info/q/getblockcount";
        String response = new TextOf(new Net(url)).asString();
        height.add(response);
      } catch (Exception e) {
        e.printStackTrace();
      }
      return height;
    }

    public static List<String> getEstimatedTransactionFee() {
      List<String> fee = new ArrayList<>();
      try {
        String url = "https://blockchain.info/q/fee";
        String response = new TextOf(new Net(url)).asString();
        fee.add(response);
      } catch (Exception e) {
        e.printStackTrace();
      }
      return fee;
    }

    public static List<String> getExchangeRates() {
      List<String> rates = new ArrayList<>();
      try {
        String url = "https://blockchain.info/q/exchange_rates";
        String response = new TextOf(new Net(url)).asString();
        String[] lines = response.split("\n");
        for (String line : lines) {
          if (line.startsWith("USD:")) {
            rates.add(line.substring(4));
          } else if (line.startsWith("EUR:")) {
            rates.add(line.substring(4));
          } else if (line.startsWith("GBP:")) {
            rates.add(line.substring(4));
          } else if (line.startsWith("CNY:")) {
            rates.add(line.substring(4));
          } else if (line.startsWith("JPY:")) {
            rates.add(line.substring(4));
          } else if (line.startsWith("KRW:")) {
            rates.add(line.substring(4));
          }
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
      return rates;
    }

  }
```