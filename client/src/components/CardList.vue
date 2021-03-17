<template>
  <transition-group name="list" tag="div">
    <v-card
      max-width="500"
      class="mx-auto"
    >
      <v-toolbar
        color="blue"
        dark
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>Gene Pool</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-clear</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-checkbox-marked-circle</v-icon>
        </v-btn>
      </v-toolbar>

      <v-list two-line>
        <v-list-item-group
          v-model="selected"
          multiple
          active-class="pink--text"
        >
          <template v-for="(item, index) in list_items">
            <v-list-item :key="item.title">
              <template v-slot:default="{ active }">
                <v-list-item-content>
                  <v-list-item-title v-text="item.title"></v-list-item-title>
                  <v-list-item-subtitle class="text--primary" v-text="item.headline"></v-list-item-subtitle>
                  <v-list-item-subtitle v-text="item.subtitle"></v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <v-list-item-action-text v-text="item.action"></v-list-item-action-text>
                  <v-icon
                    v-if="!active"
                    color="grey lighten-1"
                  >
                    star_border
                  </v-icon>

                  <v-icon
                    v-else
                    color="yellow"
                  >
                    star
                  </v-icon>
                </v-list-item-action>
              </template>
            </v-list-item>

            <v-divider
              v-if="index + 1 < items.length"
              :key="index"
            ></v-divider>
          </template>
        </v-list-item-group>
      </v-list>
    </v-card>
  </transition-group>
</template>



<template>
  <transition-group name="list" tag="div">
    <v-card v-for="(item, index) in value" :key="item[itemId]" outlined class="mt-3">
      <v-card-title class="justify-end pb-0">
        <v-btn :disabled="index + 1 >= value.length" @click="down(index)" icon>
          <v-icon>
            mdi-arrow-down
          </v-icon>
        </v-btn>
        <v-btn :disabled="index === 0" @click="up(index)" icon>
          <v-icon>
            mdi-arrow-up
          </v-icon>
        </v-btn>
        <v-btn @click="remove(index)" icon>
          <v-icon>
            mdi-close
          </v-icon>
        </v-btn>
      </v-card-title>
      <v-card-text>
        <slot :item="item" :index="index" />
      </v-card-text>
    </v-card>
  </transition-group>
</template>

<script>
export default {
  props: {
    value: {
      type: Array,
      default: () => []
    },

    itemId: {
      type: String,
      default: 'id'
    }
  },

  methods: {
    remove (index) {
      const newValue = [...this.value.slice(0, index), ...this.value.slice(index + 1)]
      this.$emit('input', newValue)
    },

    up (index) {
      const newValue = [...this.value]
      newValue[index] = this.value[index - 1]
      newValue[index - 1] = this.value[index]
      this.$emit('input', newValue)
    },

    down (index) {
      const newValue = [...this.value]
      newValue[index] = this.value[index + 1]
      newValue[index + 1] = this.value[index]
      this.$emit('input', newValue)
    }
  }
}
</script>

<style scoped>
.list-enter, .list-leave-to {
  opacity: 0;
}

.list-enter-active, .list-leave-active {
  transition: opacity 0.5s ease;
}

.list-move {
  transition: transform 0.5s ease-out;
}
</style>
