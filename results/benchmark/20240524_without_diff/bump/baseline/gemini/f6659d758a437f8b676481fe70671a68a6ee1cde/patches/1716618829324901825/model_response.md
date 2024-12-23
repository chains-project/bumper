```java
  import org.yaml.snakeyaml.introspector.Property;
  import org.yaml.snakeyaml.introspector.PropertySubstitute;
  import org.yaml.snakeyaml.introspector.PropertyUtils;
  import org.yaml.snakeyaml.nodes.NodeTuple;
  import org.yaml.snakeyaml.nodes.Tag;
  import org.yaml.snakeyaml.representer.Representer;

  import java.beans.IntrospectionException;
  import java.beans.Introspector;
  import java.beans.PropertyDescriptor;
  import java.lang.reflect.Field;
  import java.lang.reflect.Method;
  import java.lang.reflect.Modifier;
  import java.util.*;

  public class CustomRepresenter extends Representer {

      private final Map<Class<?>, Tag> classTags;
      private final Map<Class<?>, Representer> representerMap;
      private final Set<Class<?>> checkedClasses;
      private final boolean explicitPropertyUtils;
      private final boolean relaxedPropertyDetection;

      /**
       * Create a Representer for the default Representers ({@link org.yaml.snakeyaml.representer.Representer#DEFAULT_REPRESENTERS}).
       */
      public CustomRepresenter() {
          this(Representer.DEFAULT_REPRESENTERS, null, null);
      }

      /**
       * Create a Representer for the specified Representers.
       *
       * @param representers representers
       */
      public CustomRepresenter(List<Representer> representers) {
          this(representers, null, null);
      }

      /**
       * Create a Representer for the specified Representers and multi representers.
       *
       * @param representers  representers
       * @param multiRepresenter multi representers
       * @deprecated use {@link #CustomRepresenter(List, MultiRepresenter)}
       */
      @Deprecated
      public CustomRepresenter(List<Representer> representers, MultiRepresenter multiRepresenter) {
          this(representers, multiRepresenter, null);
      }

      /**
       * Create a Representer for the specified Representers and multi representers.
       *
       * @param representers representers
       * @param multiRepresenter multi representers
       */
      public CustomRepresenter(List<Representer> representers, MultiRepresenter multiRepresenter,
                                TrustedTagInspector tagInspector) {
          super(representers, multiRepresenter);
          if (tagInspector == null) {
              classTags = new HashMap<>();
              representerMap = new HashMap<>();
              checkedClasses = new HashSet<>();
              explicitPropertyUtils = false;
              relaxedPropertyDetection = false;
          } else {
              classTags = tagInspector.getClassTags();
              representerMap = tagInspector.getRepresenterMap();
              checkedClasses = tagInspector.getCheckedClasses();
              explicitPropertyUtils = tagInspector.isExplicitPropertyUtils();
              relaxedPropertyDetection = tagInspector.isRelaxedPropertyDetection();
          }
      }

      @Override
      protected NodeTuple representJavaBeanProperty(Object javaBean, Property property, Object propertyValue,
                                                    Tag customTag) {
          // if a custom tag is defined then ignore other
          if (customTag != null) {
              return representJavaBeanProperty(javaBean, property, propertyValue, customTag,
                      Tag.MAP.equals(customTag));
          }

          Class<?> type = property.getType();
          // check if the value should be represented explicitly
          if (type == null) {
              Class<?>[] params = property.getActualTypeArguments();
              if (params != null && params.length == 1 && params[0] == String.class) {
                  return representJavaBeanProperty(javaBean, property, propertyValue, Tag.STR, true);
              }
              propertyValue = representData(propertyValue);
          }
          // check if the type is a primitive or wrapper
          if (representPrimitive(propertyValue)) {
              return representJavaBeanProperty(javaBean, property, propertyValue, Tag.STR, true);
          } else {
              return super.representJavaBeanProperty(javaBean, property, propertyValue, customTag);
          }
      }

      @Override
      protected Tag getTag(Class<?> clazz, Tag customTag) {
          if (null != customTag) {
              return customTag;
          }

          // if the class is indexed by a representer use it
          Representer representer = representerMap.get(clazz);
          if (representer != null) {
              return representer.getTag();
          }

          // check if the class is a java.util type
          Tag tag = classTags.get(clazz);
          if (tag == null) {
              // use the tag if the class has a field with the tag
              tag = classWithTag(clazz, customTag);
              if (tag == null) {
                  tag = classWithTag(clazz, Tag.MAP);
                  if (tag == null) {
                      // if no tag found use the default tag
                      tag = Tag.MAP;
                  }
              }
              classTags.put(clazz, tag);
          }
          return tag;
      }

      /**
       * Represent the specified class as a YAML Node.
       *
       * @param javaBean the class to be represented as a YAML Node
       * @return the YAML Node representing the class
       */
      @Override
      public Node represent(Object javaBean) {
          if (javaBean == null) {
              return representData(null);
          }
          return super.represent(javaBean);
      }

      private Tag classWithTag(Class<?> clazz, Tag customTag) {
          // check if the class has a field with the tag
          if (customTag != null) {
              for (Field field : clazz.getDeclaredFields()) {
                  int modifiers = field.getModifiers();
                  if (Modifier.isStatic(modifiers) && Modifier.isFinal(modifiers)
                          && field.isAnnotationPresent(Tag.class)) {
                      Tag tag = field.getAnnotation(Tag.class).value();
                      if (tag.equals(customTag)) {
                          return tag;
                      }
                  }
              }
          }
          return null;
      }

      private NodeTuple representJavaBeanProperty(Object javaBean, Property property, Object propertyValue,
                                                   Tag customTag, boolean isMap) {
          Tag tag = customTag;
          if (tag == null) {
              tag = getTag(property.getType(), customTag);
          }

          NodeTuple tuple = representJavaBeanProperty(javaBean, property, propertyValue, tag);

          if (isMap) {
              if (propertyValue instanceof Map) {
                  // if it is a Map then use the name as key
                  // the value will be represented as a Node
                  tuple = new NodeTuple(representData(property.getName()), tuple.getValue());
              } else {
                  // if it is a JavaBean then recursively represent the JavaBean
                  // the value will be represented as a Node
                  tuple = new NodeTuple(representData(property.getName()), represent(propertyValue));
              }
          }

          return tuple;
      }

      @Override
      protected NodeTuple representJavaBeanProperty(Object javaBean, Property property, Object propertyValue,
                                                   Tag customTag) {
          // if a custom tag is defined then ignore other
          if (customTag != null) {
              return representJavaBeanProperty(javaBean, property, propertyValue, customTag,
                      Tag.MAP.equals(customTag));
          }

          Class<?> type = property.getType();
          // check if the value should be represented explicitly
          if (type == null) {
              Class<?>[] params = property.getActualTypeArguments();
              if (params != null && params.length == 1 && params[0] == String.class) {
                  return representJavaBeanProperty(javaBean, property, propertyValue, Tag.STR, true);
              }
              propertyValue = representData(propertyValue);
          }
          // check if the type is a primitive or wrapper
          if (representPrimitive(propertyValue)) {
              return representJavaBeanProperty(javaBean, property, propertyValue, Tag.STR, true);
          } else {
              return super.representJavaBeanProperty(javaBean, property, propertyValue, customTag);
          }
      }

      private NodeTuple representJavaBeanProperty(Object javaBean, Property property, Object propertyValue,
                                                   Tag customTag, boolean isMap) {
          Tag tag = customTag;
          if (tag == null) {
              tag = getTag(property.getType(), customTag);
          }

          NodeTuple tuple = representJavaBeanProperty(javaBean, property, propertyValue, tag);

          if (isMap) {
              if (propertyValue instanceof Map) {
                  // if it is a Map then use the name as key
                  // the value will be represented as a Node
                  tuple = new NodeTuple(representData(property.getName()), tuple.getValue());
              } else {
                  // if it is a JavaBean then recursively represent the JavaBean
                  // the value will be represented as a Node
                  tuple = new NodeTuple(representData(property.getName()), represent(propertyValue));
              }
          }

          return tuple;
      }

      /**
       * Represent the specified class as a YAML Node.
       *
       * @param javaBean the class to be represented as a YAML Node
       * @return the YAML Node representing the class
       */
      @Override
      public Node represent(Object javaBean) {
          if (javaBean == null) {
              return representData(null);
          }
          return super.represent(javaBean);
      }

      /**
       * Represent the specified class as a YAML Node.
       *
       * @param javaBean the class to be represented as a YAML Node
       * @return the YAML Node representing the class
       */
      @Override
      public Node represent(Object javaBean, Type type) {
          if (javaBean == null) {
              return representData(null);
          }
          return super.represent(javaBean, type);
      }

      private boolean representPrimitive(Object propertyValue) {
          if (propertyValue == null) {
              return true;
          }
          return propertyValue instanceof String
                  || propertyValue instanceof Boolean
                  || propertyValue instanceof Number
                  || propertyValue instanceof Date
                  || propertyValue.getClass().isPrimitive();
      }

      /**
       * Represent the specified class as a YAML Node.
       *
       * @param javaBean the class to be represented as a YAML Node
       * @return the YAML Node representing the class
       */
      @Override
      public NodeTuple representJavaBean(Object javaBean) {
          Class<?> clazz = javaBean.getClass();
          if (!checkedClasses.contains(clazz)) {
              representClass(clazz);
              checkedClasses.add(clazz);
          }
          List<NodeTuple> value = new ArrayList<>();
          try {
              PropertyUtils propertyUtils = getPropertyUtils(javaBean);
              PropertyDescriptor[] properties = propertyUtils.getPropertyDescriptors();
              for (PropertyDescriptor property : properties) {
                  Method readMethod = property.getReadMethod();
                  if (readMethod != null) {
                      Property substitute = propertyUtils.getPropertySubstitute(readMethod);
                      if (substitute == null) {
                          Object propertyValue = readMethod.invoke(javaBean);
                          value.add(representJavaBeanProperty(javaBean, property, propertyValue, null));
                      } else {
                          Object propertyValue = substitute.getSubstitute(javaBean);
                          value.add(representJavaBeanProperty(javaBean, property, propertyValue, null));
                      }
                  }
              }
          } catch (Exception e) {
              throw new YAMLException(e);
          }
          return new NodeTuple(representData(clazz), value);
      }

      private PropertyUtils getPropertyUtils(Object javaBean) throws IntrospectionException {
          if (explicitPropertyUtils) {
              return new PropertyUtils();
          }
          PropertyUtils propertyUtils = new PropertyUtils();
          String[] ignoredProperties = getIgnoredProperties(javaBean);
          if (ignoredProperties != null) {
              propertyUtils.setIgnoreProperties(ignoredProperties);
          }
          propertyUtils.setRelaxedPropertyDetection(relaxedPropertyDetection);
          return propertyUtils;
      }

      protected String[] getIgnoredProperties(Object javaBean) {
          return null;
      }

      protected void representClass(Class<?> clazz) {
          if (Introspector.getBeanInfo(clazz, Introspector.IGNORE_ALL_BEANINFO) == null) {
              return;
          }
          if (clazz.getSuperclass() != null) {
              representClass(clazz.getSuperclass());
          }
          List<NodeTuple> value = new ArrayList<>();
          try {
              PropertyUtils propertyUtils = getPropertyUtils(null);
              PropertyDescriptor[] properties = propertyUtils.getPropertyDescriptors();
              for (PropertyDescriptor property : properties) {
                  Method readMethod = property.getReadMethod();
                  if (readMethod != null
                          && (readMethod.getDeclaringClass().isAssignableFrom(clazz) || readMethod.isAnnotationPresent(PropertySubstitute.class))) {
                      Property substitute = propertyUtils.getPropertySubstitute(readMethod);
                      if (substitute == null) {
                          Class<?>[] params = readMethod.getParameterTypes();
                          if (params.length == 1 && "name".equals(readMethod.getName()) && String.class.isAssignableFrom(params[0])) {
                              value.add(representJavaBeanProperty(null, property, readMethod.invoke(null, clazz.getName()), null));
                          } else if (params.length == 0 && readMethod.getReturnType() == Class.class && "class".equals(readMethod.getName())) {
                              value.add(representJavaBeanProperty(null, property, readMethod.invoke(null), null));
                          }
                      } else {
                          value.add(representJavaBeanProperty(null, property, substitute.getSubstitute(null), null));
                      }
                  }
              }
          } catch (Exception e) {
              throw new YAMLException(e);
          }
          if (!value.isEmpty()) {
              addClassTag(clazz, value);
          }
      }

      protected void addClassTag(Class<?> clazz, List<NodeTuple> value) {
          Tag customTag = classWithTag(clazz, null);
          if (customTag != null) {
              representerMap.put(clazz, new Representer(this));
          } else {
              if (value.size() == 1) {
                  NodeTuple tuple = value.get(0);
                  if (tuple.getValueValue() instanceof Node) {
                      representerMap.put(clazz, new Representer(this));
                  }
              }
          }
      }
  }
```