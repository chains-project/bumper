```java
  /**
     * Sets the private registry value of {@link DefaultMOServer} via reflection.
     * FIXME
     * If there is any possibility to avoid this, then replace!
     *
     * @param group {@link ManagedObject} to register.
     */
    private void registerHard(final MOGroup group) {
        try {
            final Field registry = server.getClass().getDeclaredField("registry");
            registry.setAccessible(true);
            final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
            DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
            reg.put(contextScope, group);
            // ++ new line
            registry.set(server, new SortedMap<MOScope, ManagedObject>() {
                @Override
                public Comparator<? super MOScope> comparator() {
                    return reg.comparator();
                }

                @Override
                public SortedMap<MOScope, ManagedObject> subMap(MOScope fromKey, MOScope toKey) {
                    return reg.subMap(fromKey, toKey);
                }

                @Override
                public SortedMap<MOScope, ManagedObject> headMap(MOScope toKey) {
                    return reg.headMap(toKey);
                }

                @Override
                public SortedMap<MOScope, ManagedObject> tailMap(MOScope fromKey) {
                    return reg.tailMap(fromKey);
                }

                @Override
                public MOScope firstKey() {
                    return reg.firstKey();
                }

                @Override
                public MOScope lastKey() {
                    return reg.lastKey();
                }

                @Override
                public int size() {
                    return reg.size();
                }

                @Override
                public boolean isEmpty() {
                    return reg.isEmpty();
                }

                @Override
                public boolean containsKey(Object key) {
                    return reg.containsKey(key);
                }

                @Override
                public boolean containsValue(Object value) {
                    return reg.containsValue(value);
                }

                @Override
                public ManagedObject get(Object key) {
                    return reg.get(key);
                }

                @Override
                public ManagedObject put(MOScope key, ManagedObject value) {
                    return reg.put(key, value);
                }

                @Override
                public ManagedObject remove(Object key) {
                    return reg.remove(key);
                }

                @Override
                public void putAll(Map<? extends MOScope, ? extends ManagedObject> m) {
                    reg.putAll(m);
                }

                @Override
                public void clear() {
                    reg.clear();
                }

                @Override
                public Set<MOScope> keySet() {
                    return reg.keySet();
                }

                @Override
                public Collection<ManagedObject> values() {
                    return reg.values();
                }

                @Override
                public Set<Entry<MOScope, ManagedObject>> entrySet() {
                    return reg.entrySet();
                }
            });
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```